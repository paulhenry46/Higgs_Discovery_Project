import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import uproot
import vector
import awkward as ak

# Configurer Pandas pour afficher plus de colonnes
pd.set_option('display.max_columns', None)

# --- 1. DÉFINITION DES CHEMINS ET CONSTANTES ---

# Fichiers de simulation Monte Carlo pour le fond (background) ZZ -> 4l
# NOTE: Ces chemins sont des exemples et DOIVENT être ajustés
MC_BACKGROUND_FILES = {
    'ZZTo4mu': '../../data/12940/ZZTo4mu.root',
    'ZZTo4e': '../../data/12938/ZZTo4e.root',
    'ZZTo2e2mu_2mu': '../../data/12939/ZZTo2e2mu.root',  # Muons pour 2e2mu
    'ZZTo2e2mu_2e': '../../data/12939/ZZTo2e2mu.root'    # Electrons pour 2e2mu
}

# Nombre total d'événements générés dans la simulation pour chaque échantillon (EXEMPLE)
# IMPORTANT: Remplacez par vos N_MC_total exacts !
N_GEN_DATA_ZZ = {
    'ZZTo4mu': 1000000,
    'ZZTo4e': 950000,
    'ZZTo2e2mu_2mu': 1700000,
    'ZZTo2e2mu_2e': 1650000
}

# Luminosité intégrée du run d'acquisition (en fb^-1) - EXEMPLE 2012
LUMINOSITY_INV_FB = 12.1

# Section efficace théorique (cross-section, en femtobarns, fb)
# ZZ -> 4l est le fond principal
MC_CROSS_SECTIONS_FB = {
    "ZZTo4L_GLOBAL_SIGMA": 17600.0, # Section efficace globale pour ZZ -> 4l
}

TREE_NAME = 'leptons'
MAX_EVENTS_PER_FILE = 100000 # Limite pour le test


# --- 2. FONCTIONS DE CHARGEMENT ET PRÉ-TRAITEMENT ---

def load_and_flatten_data(file_path, tree_name, max_events, required_columns, flavor_filter=None):
    """Charge les données d'un fichier ROOT, applique un filtre de saveur et met à plat."""
    try:
        with uproot.open(file_path) as file:
            tree = file[tree_name]
            if tree.num_entries == 0:
                print(f"Avertissement: Arbre vide dans {file_path}.")
                return pd.DataFrame()

            n_entries = min(tree.num_entries, max_events)
            print(f"  -> Chargement max {n_entries} événements de {file_path}...")

            # Chargement dans un DataFrame Pandas
            data = tree.arrays(required_columns, entry_stop=n_entries, library="pd")

            # Mettre à plat (flatten) et créer event_id/lepton_idx
            data = data.reset_index().rename(columns={'entry': 'event_id', 'subentry': 'lepton_idx'})

            # Appliquer le filtre de saveur si spécifié (11=electron, 13=muon)
            if flavor_filter is not None:
                data = data[data['flavor'] == flavor_filter]
            
            # Ajouter la source
            data['source'] = os.path.basename(file_path).split('.')[0]
            data.rename(columns={'event': 'event_id'}, inplace=True) # Assurer la cohérence du nom de la colonne d'événement

            return data

    except FileNotFoundError:
        print(f"ERREUR: Fichier non trouvé: {file_path}")
        return pd.DataFrame()
    except Exception as e:
        print(f"ERREUR lors du chargement des données de {file_path}: {e}")
        return pd.DataFrame()

def apply_quality_cuts(df):
    """Applique les coupures d'ID, d'Isolation, Pt et Eta."""
    if df.empty:
        return df
        
    # Coupure d'ID et d'Isolation (valeurs typiques pour le signal)
    df_id_iso = df[(df['id'] == 1) & (df['iso'] < 0.35)]

    # Coupure en Pt et Eta (cinématique)
    df_kin = df_id_iso[(df_id_iso['pt'] > 5.0) & (np.abs(df_id_iso['eta']) < 2.4)]
    
    print(f"  -> Lepton retaine après coupures de qualité: {len(df_kin)}")
    return df_kin.copy()

def add_lorentz_vectors(df):
    """Ajoute une colonne 'lv' contenant le vecteur de Lorentz pour chaque lepton."""
    if df.empty:
        return df

    try:
        vector_array_temp = vector.array({
            "pt": df["pt"],
            "eta": df["eta"],
            "phi": df["phi"],
            "mass": df["mass"]
        })
        df['lv'] = vector_array_temp
        return df
    except Exception as e:
        print(f"\nCRITICAL ERROR lors de la création de 'lv': {e}")
        return df

def load_and_prepare_mc_data():
    """Fonction principale pour charger et préparer tous les échantillons MC."""
    all_mc_leptons = []
    required_cols = ['event', 'pt', 'eta', 'phi', 'mass', 'charge', 'flavor', 'id', 'iso']
    
    for sample_name, file_path in MC_BACKGROUND_FILES.items():
        flavor_filter = None
        if '2mu' in sample_name: 
            flavor_filter = 13  # Muons
        elif '2e' in sample_name: 
            flavor_filter = 11  # Electrons
            
        df = load_and_flatten_data(file_path, TREE_NAME, MAX_EVENTS_PER_FILE, required_cols, flavor_filter=flavor_filter)
        if not df.empty:
            all_mc_leptons.append(df)

    if not all_mc_leptons:
        print("ERREUR: Aucun échantillon MC n'a pu être chargé.")
        return pd.DataFrame()
        
    full_df = pd.concat(all_mc_leptons, ignore_index=True)
    cleaned_df = apply_quality_cuts(full_df)
    final_df = add_lorentz_vectors(cleaned_df)
    
    print(f"\nTotal MC leptons (après coupures): {len(final_df)}")
    return final_df


# --- 3. FONCTIONS DE SÉLECTION DU HIGGS (Z1, Z2) ---

Z_MASS_PDG = 91.1876 # Masse nominale du boson Z (GeV)

def combine_leptons(df):
    """Crée tous les quadruplets de leptons possibles dans chaque événement."""
    events = df.groupby('event_id').filter(lambda x: len(x) >= 4)
    events_list = events['event_id'].unique()
    print(f"\nÉvénements avec >= 4 leptons de qualité : {len(events_list)}")
    
    quadruplets = []
    for event_id, event_group in events.groupby('event_id'):
        leptons = event_group.reset_index()
        indices = leptons.index.tolist()
        
        # Création combinatoire de quadruplets
        for i in range(len(indices)):
            for j in range(i + 1, len(indices)):
                for k in range(j + 1, len(indices)):
                    for l in range(k + 1, len(indices)):
                        quadruplets.append({
                            'event_id': event_id,
                            'l1': leptons.loc[indices[i]], 'l2': leptons.loc[indices[j]],
                            'l3': leptons.loc[indices[k]], 'l4': leptons.loc[indices[l]]
                        })
                        
    return pd.DataFrame(quadruplets)

def apply_event_cuts(df):
    """Applique les coupures d'événement (charge totale nulle et Pt_min)."""
    initial_count = len(df)
    if initial_count == 0:
        return df
        
    # Coupure de Charge Totale : Q_total = 0
    df['q_total'] = df['l1'].apply(lambda x: x['charge']) + df['l2'].apply(lambda x: x['charge']) + \
                    df['l3'].apply(lambda x: x['charge']) + df['l4'].apply(lambda x: x['charge'])
    df_charge = df[df['q_total'] == 0].copy()
    
    # Coupure en Pt Minimum : le lepton le plus mou doit avoir Pt > 5 GeV
    min_pt_list = df_charge.apply(lambda row: min(
        row['l1']['pt'], row['l2']['pt'], row['l3']['pt'], row['l4']['pt']
    ), axis=1)
    
    df_charge['pt_min'] = min_pt_list
    df_final = df_charge[df_charge['pt_min'] > 5.0]
    
    print(f"Coupures d'événement (Q=0, Pt_min>5): {len(df_final)} / {initial_count} quadruplets retenus.")
    return df_final.copy()

def find_z_candidates(df_quad):
    """Trouve la meilleure paire Z1 (la plus proche de Mz) et Z2 (la paire SFOC restante) et calcule M4l."""
    best_candidates = []
    
    for event_id, event_group in df_quad.groupby('event_id'):
        best_candidate = None
        min_mass_diff_z1 = float('inf')
        
        for _, quad in event_group.iterrows():
            # Récupérer les informations des 4 leptons du quadruplet
            leptons_data = [quad['l1'], quad['l2'], quad['l3'], quad['l4']]
            leptons_lv = [d['lv'] for d in leptons_data]
            charges = [d['charge'] for d in leptons_data]
            flavors = [d['flavor'] for d in leptons_data]
            
            # 1. Sélection Z1 (paire SFOC la plus proche de Mz)
            z1_pair = None
            min_z1_mass_diff = float('inf')
            indices_pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
            
            for i, j in indices_pairs:
                # Same Flavor, Opposite Charge (SFOC)
                if flavors[i] == flavors[j] and charges[i] == -charges[j]:
                    z_mass = (leptons_lv[i] + leptons_lv[j]).mass
                    if np.abs(z_mass - Z_MASS_PDG) < min_z1_mass_diff:
                        min_z1_mass_diff = np.abs(z_mass - Z_MASS_PDG)
                        z1_pair = (i, j, z_mass)
                        
            if z1_pair is None: continue 
                
            # 2. Sélection Z2 (paire SFOC restante)
            # Les indices restants forment Z2
            all_indices = {0, 1, 2, 3}
            remaining_indices = list(all_indices - {z1_pair[0], z1_pair[1]})
            k, l = remaining_indices[0], remaining_indices[1]
            
            z2_pair = None
            if flavors[k] == flavors[l] and charges[k] == -charges[l]:
                z2_mass = (leptons_lv[k] + leptons_lv[l]).mass
                z2_pair = (k, l, z2_mass)
            
            if z2_pair is None: continue 
                
            # 3. Coupures de Masse Invariante Z1 et Z2
            z1_mass = z1_pair[2]
            z2_mass = z2_mass
            
            if not (40.0 < z1_mass < 120.0 and 12.0 < z2_mass < 120.0):
                continue
                
            # 4. Calcul de M4l
            h_mass = sum(leptons_lv).mass
            
            # 5. Sélection du Meilleur Candidat H (le Z1 le plus proche de Mz)
            if np.abs(z1_mass - Z_MASS_PDG) < min_mass_diff_z1:
                min_mass_diff_z1 = np.abs(z1_mass - Z_MASS_PDG)
                best_candidate = {
                    'event_id': event_id,
                    'z1_mass': z1_mass,
                    'z2_mass': z2_mass,
                    'h_mass': h_mass,
                }
                
        if best_candidate is not None:
            best_candidates.append(best_candidate)
            
    df_final = pd.DataFrame(best_candidates)
    
    # Coupure de masse H -> 4l pour la région d'intérêt
    df_final = df_final[(100.0 < df_final['h_mass']) & (df_final['h_mass'] < 160.0)]
    
    print(f"\nTotal candidats H -> 4l retenus (après Z1/Z2 et M4l [100, 160]): {len(df_final)}")
    return df_final.copy()


# --- 4. FONCTIONS DE POIDS ET DE NORMALISATION MC ---

def calculate_mc_weight(cross_section_fb: float, n_mc_total: int) -> float:
    """
    Calcule le facteur de poids MC (normalisation) : W = (L * sigma) / N_MC_total
    """
    print(f"\n--- Détails du Calcul de Poids MC ---")
    print(f"Luminosité (L)       : {LUMINOSITY_INV_FB} fb⁻¹")
    print(f"Section Efficace (σ) : {cross_section_fb} fb")
    print(f"N_MC_total           : {n_mc_total}")
    
    if n_mc_total <= 0:
        print("Avertissement: N_MC_total est nul. Poids retourné: 0.0.")
        return 0.0
    
    weight_factor = (LUMINOSITY_INV_FB * cross_section_fb) / n_mc_total
    
    print(f"Facteur de Poids MC  : {weight_factor:.8f}")
    
    return weight_factor

def apply_weight_to_df(df, weight_factor):
    """Ajoute une colonne 'weight' au DataFrame avec le facteur calculé."""
    if df.empty:
        return df
        
    df['weight'] = weight_factor
    print(f"Poids MC {weight_factor:.8f} appliqué à {len(df)} événements.")
    return df


# --- 5. FONCTION DE TRACÉ ---

def plot_higgs_mass(df, weights=None):
    """Trace l'histogramme de la masse invariante M4l, avec normalisation optionnelle."""
    if df.empty:
        print("Impossible de tracer l'histogramme, le DataFrame est vide.")
        return
        
    plt.figure(figsize=(10, 6))
    
    if weights is not None and not df['weight'].isnull().all():
        # Utiliser les poids pour la normalisation
        plt.hist(df['h_mass'], bins=30, range=(100, 160), weights=weights, 
                 histtype='stepfilled', color='lightblue', edgecolor='black', 
                 label=f'MC $ZZ \\to 4\\ell$ (Normalisé à {LUMINOSITY_INV_FB} $fb^{{-1}}$)')
        plt.ylabel('Nombre d\'événements Normalisés')
    else:
        # Tracer les comptes bruts si les poids ne sont pas fournis
        plt.hist(df['h_mass'], bins=30, range=(100, 160), 
                 histtype='step', color='red', linewidth=2, 
                 label='MC $ZZ \\to 4\\ell$ (Comptes Bruts)')
        plt.ylabel('Nombre d\'événements (Comptes Bruts)')

    plt.xlabel('Masse Invariante $M_{4\\ell}$ (GeV)')
    plt.title('Distribution de $M_{4\\ell}$ pour le Fond MC $ZZ \\to 4\\ell$')
    plt.grid(axis='y', alpha=0.5)
    plt.legend()
    plt.show()
    print("\nAnalyse MC terminée. Interprétez cet histogramme pour le fond normalisé.")

# --- 6. BLOC D'EXÉCUTION PRINCIPAL ---

if __name__ == '__main__':
    print("--- DÉBUT DE L'ANALYSE H -> 4l (Monte Carlo) ---")
    
    # Étape 1: Chargement et Préparation des Données MC
    cleaned_leptons_df_mc = load_and_prepare_mc_data()

    if cleaned_leptons_df_mc.empty:
        print("\nAnalyse arrêtée : Le DataFrame MC est vide.")
        exit()

    # Étape 2: Sélection des Candidats 4-Leptons
    all_quadruplets_df_mc = combine_leptons(cleaned_leptons_df_mc)
    four_lepton_candidates_df_mc = apply_event_cuts(all_quadruplets_df_mc)

    if four_lepton_candidates_df_mc.empty:
        print("\nAnalyse arrêtée : Aucun candidat 4-lepton n'a passé les coupures d'événement.")
        exit()
        
    # Étape 3: Calcul du Poids Global MC
    files_to_sum = list(N_GEN_DATA_ZZ.keys())
    total_n_generated_zz = sum(N_GEN_DATA_ZZ.get(key, 0) for key in files_to_sum)
    TOTAL_CROSS_SECTION = MC_CROSS_SECTIONS_FB.get('ZZTo4L_GLOBAL_SIGMA', 0.0)
    
    GLOBAL_MC_WEIGHT = calculate_mc_weight(
        cross_section_fb=TOTAL_CROSS_SECTION, 
        n_mc_total=total_n_generated_zz
    )

    # Étape 4: Sélection Z1/Z2 et Calcul de M4l
    z_boson_df_mc = find_z_candidates(four_lepton_candidates_df_mc)

    # Étape 5: Application du Poids et Tracé
    if not z_boson_df_mc.empty:
        z_boson_df_mc = apply_weight_to_df(z_boson_df_mc, GLOBAL_MC_WEIGHT)
        
        print("\n--- Aperçu des Candidats H -> 4l MC (M4l) ---")
        print(z_boson_df_mc[['event_id', 'z1_mass', 'z2_mass', 'h_mass', 'weight']].head())
        
        # Tracé avec la normalisation
        plot_higgs_mass(z_boson_df_mc, weights=z_boson_df_mc['weight'])
    else:
        print("\nAucun candidat final après la sélection Z. Impossible de tracer l'histogramme.")
