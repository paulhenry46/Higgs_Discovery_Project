import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from itertools import combinations

Z_MASS = 91.1876

# List of the ROOT files downloaded.
DATA_FILES = {
    "DoubleMuon_B": "../../data/12365/Run2012B_DoubleMuParked.root",
    "DoubleMuon_C": "../../data/12366/Run2012C_DoubleMuParked.root",
    "DoubleElectron_B": "../../data/12367/Run2012B_DoubleElectron.root",
    "DoubleElectron_C": "../../data/12368/Run2012C_DoubleElectron.root"
}

BASE_CHUNK = "../../data/"

# Number of events to load
MAX_EVENTS = 1000000

try:
    import uproot # For reading CERN ROOT files
    import vector # For fast, correct Lorentz Vector calculations
    import awkward as ak # For manipulating variable-length lists
    print("Success: uproot, vector, and awkward are loaded.")

    # Necessary branches (columns) for each lepton type.
    MUON_BRANCHES = ["event", "Muon_pt", "Muon_eta", "Muon_phi", "Muon_mass", "Muon_charge", "Muon_pfRelIso03_all"]
    ELECTRON_BRANCHES = ["event", "Electron_pt", "Electron_eta", "Electron_phi", "Electron_mass", "Electron_charge", "Electron_pfRelIso03_all"]

except ImportError:
    print("Error: uproot, vector, or awkward not found. Please install these libraries to continue.")
    exit()


def load_data_from_file(file_path, file_key, range_start, range_end):
    """
    Loads specific lepton data (Muon or Electron) based on the trigger file type (file_key).
    Returns a flattened DataFrame for that file.
    """

    # 1. Determine the branches to load based on the trigger type
    if ("DoubleMuon" in file_key) or ("4mu" in file_key):
        lepton_prefix = "Muon"  # Capitalized to match branch names
        branches = MUON_BRANCHES
        flavor_pdg = 13 # Muon
    elif ("DoubleElectron" in file_key) or ("4e" in file_key):
        lepton_prefix = "Electron" # Capitalized to match branch names
        branches = ELECTRON_BRANCHES
        flavor_pdg = 11 # Electron
    else:
        print(f"Warning: Unrecognized file type ({file_key}). Skipped.")
        return pd.DataFrame()

    try:
        # Open the ROOT file and read the 'Events' tree (TTree)
        with uproot.open(file_path) as file:
            tree = file["Events"]

            # Read only the necessary branches for this file
            raw_data = tree.arrays(
                branches,
                entry_start=range_start,
                entry_stop=range_end,
                library="ak"
            )

            # --- CONVERSION TO 'FLATTENED' FORMAT (CORRECTED) ---

            # Initialize the dictionary for the flat DataFrame
            flattened_data = {}

            # 1. Handle Event ID (Repeat the Event ID for each lepton it contains)
            event_ids = raw_data['event']

            # We use the pT branch to determine the number of leptons per event
            lepton_counts = ak.num(raw_data[f'{lepton_prefix}_pt'])

            # Robust conversion to NumPy for np.repeat
            lepton_counts_np = ak.to_numpy(lepton_counts).astype(np.int64)
            event_ids_np = ak.to_numpy(event_ids).astype(np.int64)

            # Repeat the Event ID as many times as there are leptons
            flattened_data['event_id'] = np.repeat(event_ids_np, lepton_counts_np)

            # Kinematics
            flattened_data['pt'] = ak.to_numpy(ak.flatten(raw_data[f'{lepton_prefix}_pt']))
            flattened_data['eta'] = ak.to_numpy(ak.flatten(raw_data[f'{lepton_prefix}_eta']))
            flattened_data['phi'] = ak.to_numpy(ak.flatten(raw_data[f'{lepton_prefix}_phi']))
            flattened_data['mass'] = ak.to_numpy(ak.flatten(raw_data[f'{lepton_prefix}_mass']))
            flattened_data['charge'] = ak.to_numpy(ak.flatten(raw_data[f'{lepton_prefix}_charge']))

            # Isolation
            iso_key = f'{lepton_prefix}_pfRelIso03_all'
            flattened_data['iso'] = ak.to_numpy(ak.flatten(raw_data[iso_key]))

            df = pd.DataFrame(flattened_data)

            # --- KEY CORRECTION: ENFORCE NUMERIC TYPING FOR 'VECTOR' ---
            kinematic_cols = ['pt', 'eta', 'phi', 'mass']
            for col in kinematic_cols:
                # Ensure kinematic columns are of standard float64 type
                if col in df.columns:
                    df[col] = df[col].astype(np.float64)

            # Add the flavor identification column (PDG ID)
            df['flavor'] = flavor_pdg
            return df

    except Exception as e:
        # Leave a clearer message for the user
        print(f"\nERROR: Could not load file {file_path}. Does the file exist and contain an 'Events' TTree?")
        print(f"Error details: {e}")
        return pd.DataFrame()
    

def apply_quality_cuts(df):
    """
    Applies the minimal quality and kinematic cuts to individual leptons.
    This is the first essential filtering step in the H -> 4l analysis.
    """

    # A. KINEMATIC CUT ON PT (Transverse Momentum)
    pt_cut = 5.0
    df_pt_filtered = df[df['pt'] > pt_cut]

    # B. ACCEPTANCE CUT ON ETA (Pseudorapidity)
    eta_max = 2.5
    df_eta_filtered = df_pt_filtered[np.abs(df_pt_filtered['eta']) < eta_max]

    # C. ISOLATION CUT (Rejecting Leptons from Jets)
    iso_cut = 0.3
    df_final = df_eta_filtered[df_eta_filtered['iso'] < iso_cut]

    return df_final.reset_index(drop=True)

def clean_kinematic_data(df):
    """
    Corrects negative masses (reconstruction fault) and cleans invalid values
    to ensure that 'vector.array' does not crash.
    """
    initial_count = len(df)
    kinematic_cols = ['pt', 'eta', 'phi', 'mass']

    # 1. CORRECTION: Identify and correct negative masses (the main problem)
    negative_mass_mask = df['mass'] < 0
    num_neg_mass = negative_mass_mask.sum()

    if num_neg_mass > 0:
        # Warning and correction: force unphysical masses to 0.0
        df.loc[negative_mass_mask, 'mass'] = 0.1

    # 2. CLEANUP: Mask for NaN/Inf (all columns must be finite)
    is_finite = np.all(np.isfinite(df[kinematic_cols].values), axis=1)

    # 3. CLEANUP: Mask for pT > 0 (mass is now >= 0 thanks to step 1)
    pt_ok = df['pt'] > 0

    # Combined mask for valid data that remains inside
    valid_mask = is_finite & pt_ok

    df_cleaned = df[valid_mask].reset_index(drop=True)
    removed_count = initial_count - len(df_cleaned)

    return df_cleaned

def group_leptons_by_event_with_diagnostic_data(df):
    """
    Groups leptons by event, filtering to keep only events that meet the H -> 4l criteria
    (4 leptons + zero net charge) AND returns the 'Before Charge Cut' data for diagnostics.
    """
    initial_events = df['event_id'].nunique()
    
    # STEP 1: TEMPORARILY REMOVE THE VECTOR COLUMN FOR SAFE FILTERING
    # We create a safe version of the DataFrame without the toxic 'lv' column
    kinematic_df = df.drop(columns=['lv']) if 'lv' in df.columns else df
    
    # STEP 2: GROUP AND FILTER BASED ON BASE COLUMNS
    event_groups = kinematic_df.groupby('event_id')
    event_counts = event_groups.size()
    event_net_charge = event_groups['charge'].sum()
    
    # STEP3: DIAGNOSTIC DATA GATHERING
    # Calculate the set of IDs for ALL 4-lepton events BEFORE the charge cut
    four_lepton_events_ids = event_counts[event_counts == 4].index 
    #Since the index of event_counts is the event_id, this returns a pandas Index object containing a list of all event IDs that satisfy the 4-lepton requirement.
    
    # DataFrame for the 'Before Charge Cut' plot data
    # This contains all events with 4 leptons, regardless of charge sum.
    df_before_charge_cut = kinematic_df[kinematic_df['event_id'].isin(four_lepton_events_ids)].reset_index(drop=True)

    # STEP 4: FINAL FILTERING
    zero_net_charge_events = event_net_charge[event_net_charge == 0].index
    
    # Combine the 4-lepton requirement and the zero net charge requirement
    valid_event_ids = four_lepton_events_ids.intersection(zero_net_charge_events)
    
    # Select final condidates
    df_4l = kinematic_df[kinematic_df['event_id'].isin(valid_event_ids)].reset_index(drop=True)

    # STEP 5: REGENERATE AND RE-ATTACH THE VECTOR COLUMN to the FINAL DF
    if not df_4l.empty and 'lv' in df.columns:
        new_vector_array = vector.array({
            "pt": df_4l['pt'], "eta": df_4l["eta"], 
            "phi": df_4l["phi"], "mass": df_4l["mass"]
        })
        df_4l['lv'] = new_vector_array

    # Return the FINAL data and the DIAGNOSTIC data
    return df_4l, df_before_charge_cut

def find_z_candidates(df):
    """
    Finds the Z1 and Z2 candidates using Lorentz vectors (df['lv']).
    This is where the M4l (Higgs mass) calculation is performed.
    """
    z_candidates = []
    df_lite = df.drop(columns=['lv']) if 'lv' in df.columns else df
    
    df_lite['original_index'] = df_lite.index
    
    grouped = df_lite.groupby('event_id')
    
    for event_id, leptons_in_event in grouped:
        
        sfos_pairs = []
        
         # 1. Find all SFOS (Same-Flavor, Opposite-Sign) pairs
        for l1_idx, l2_idx in combinations(leptons_in_event.index, 2):
            l1 = leptons_in_event.loc[l1_idx]
            l2 = leptons_in_event.loc[l2_idx]
            
            # SFOS Condition (Same Flavor, Opposite Sign)
            if (l1['flavor'] == l2['flavor']) and (l1['charge'] * l2['charge'] < 0):

                try:
                    # Retrieve Lorentz vectors from the original DataFrame
                    l1_lv = df.loc[l1_idx, 'lv']
                    l2_lv = df.loc[l2_idx, 'lv']
                    # Using Lorentz vector addition to calculate the pair's four-vector
                    l_pair = l1_lv + l2_lv
                    m_inv = l_pair.mass
                except Exception as e:
                    continue 

                # Cleaning up NaNs or Infs resulting from vector addition
                if not np.isfinite(m_inv):
                    continue

                sfos_pairs.append({
                    'mass': m_inv,
                    'l1_idx': l1_idx,
                    'l2_idx': l2_idx,
                    'abs_diff_z': np.abs(m_inv - Z_MASS) # Critère Z1
                })
        
        if len(sfos_pairs) < 2:
            continue 

        # 2. Select the Z1 candidate (closest to M_Z) 
        sfos_pairs.sort(key=lambda x: x['abs_diff_z'])
        z1_candidate = sfos_pairs[0]
        
        used_indices = {z1_candidate['l1_idx'], z1_candidate['l2_idx']}

        # 3. Select the Z2 candidate
        
        best_z1_combo = None
        min_total_diff = np.inf
        
        # Iterate over ALL SFOS pairs to find the best orthogonal Z2
        for pair_z2 in sfos_pairs:
            
            # Z2 must not share a lepton with Z1
            z2_indices = {pair_z2['l1_idx'], pair_z2['l2_idx']}
            if len(used_indices.intersection(z2_indices)) == 0:
                
                # Calculate optimization metric (Minimize |M_Z1 - M_Z| + |M_Z2 - M_Z|)
                current_total_diff = z1_candidate['abs_diff_z'] + pair_z2['abs_diff_z']
                
                # We search for the best orthogonal pair remaining which minimizes the total deviation (D).
                
                if current_total_diff < min_total_diff:
                    min_total_diff = current_total_diff
                    best_z1_combo = {
                        'z1': z1_candidate,
                        'z2': pair_z2
                    }

                
        if best_z1_combo:

            z1_candidate = best_z1_combo['z1']
            z2_candidate = best_z1_combo['z2']
            
            # Retrieve the 4 Lorentz vectors for the final leptons
            l1_lv = df.loc[z1_candidate['l1_idx'], 'lv']
            l2_lv = df.loc[z1_candidate['l2_idx'], 'lv'] 
            l3_lv = df.loc[z2_candidate['l1_idx'], 'lv']
            l4_lv = df.loc[z2_candidate['l2_idx'], 'lv']
            
            # Calculate Higgs Mass (M4l)
            h_lv = l1_lv + l2_lv + l3_lv + l4_lv
            h_mass = h_lv.mass
            
            if not np.isfinite(h_mass):
                continue
            
            z_candidates.append({
                'event_id': event_id,
                'z1_mass': z1_candidate['mass'],
                'z2_mass': z2_candidate['mass'],
                'mass': h_mass, 
                'l_indices': list(used_indices) + [z2_candidate['l1_idx'], z2_candidate['l2_idx']]
            })

    z_df = pd.DataFrame(z_candidates)
    
    print(f"\nTotal events with at least two SFOS pairs (Z1+Z2) : {len(z_df)}")
    z_df = z_df[['event_id', 'mass']]
    return z_df

def get_higgs_candidates(df):
        filtered_leptons_df = apply_quality_cuts(df)
        cleaned_leptons_df = clean_kinematic_data(filtered_leptons_df)
        # 4. CREATION OF LORENTZ VECTORS ON ALL FILTERED DATA (The right way)
        vector_array_temp = vector.array({
                "pt": cleaned_leptons_df['pt'],
                "eta": cleaned_leptons_df["eta"],
                "phi": cleaned_leptons_df["phi"],
                "mass": cleaned_leptons_df["mass"]
            })

        cleaned_leptons_df['lv'] = vector_array_temp
        four_lepton_candidates_df, all_four_leptons_df = group_leptons_by_event_with_diagnostic_data(cleaned_leptons_df)
        
        return find_z_candidates(four_lepton_candidates_df)



#----------MAIN EXECUTION------------
print("--- START OF H -> 4l ANALYSIS (Real Data) ---")



all_dfs = []

for key, file_path in DATA_FILES.items():
    if os.path.exists(file_path):
        range_start = 0
        range_end = MAX_EVENTS
        with uproot.open(file_path) as file:
            tree = file["Events"]
            n_entries = tree.num_entries
        i=0
        while range_end < n_entries:
            output_filename = BASE_CHUNK + key + "_" + str(i) + ".csv"
            if range_end > n_entries:
                range_end = n_entries

            df = load_data_from_file(file_path, key, range_start, range_end)
            z_boson_df = get_higgs_candidates(df)
            print(f"   Chunk {i}: Writing {len(df)} analyzed events to {output_filename}")
            print(f" Range {range_end} / {n_entries}")
        
            z_boson_df.to_csv(output_filename, header=True, index=False)
            range_end = range_end + MAX_EVENTS
            range_start = range_start + MAX_EVENTS
            i = i+1