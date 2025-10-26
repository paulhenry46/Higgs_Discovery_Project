import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from itertools import combinations

# --- CONFIGURATION (UPDATED for Multi-File Analysis) ---

# List of the ROOT files you have downloaded.
# These names must exactly match the files on your file system.
DATA_FILES = {
    "DoubleMuon_B": "../../data/12365/Run2012B_DoubleMuParked.root",
    "DoubleMuon_C": "../../data/12366/Run2012C_DoubleMuParked.root",
    "DoubleElectron_B": "../../data/12367/Run2012B_DoubleElectron.root",
    "DoubleElectron_C": "../../data/12368/Run2012C_DoubleElectron.root"
}

# Number of events to load (use a small number for a quick test)
MAX_EVENTS = 100000

# --- 1. LIBRARIES FOR REAL DATA HANDLING ---
try:
    import uproot # For reading CERN ROOT files
    import vector # For fast, correct Lorentz Vector calculations
    import awkward as ak # For manipulating variable-length lists
    print("Success: uproot, vector, and awkward are loaded.")

    # Necessary branches (columns) for each lepton type.
    # IMPORTANT: Added the "event" branch for handling event IDs.
    MUON_BRANCHES = ["event", "Muon_pt", "Muon_eta", "Muon_phi", "Muon_mass", "Muon_charge", "Muon_pfRelIso03_all"]
    ELECTRON_BRANCHES = ["event", "Electron_pt", "Electron_eta", "Electron_phi", "Electron_mass", "Electron_charge", "Electron_pfRelIso03_all"]

except ImportError:
    print("Error: uproot, vector, or awkward not found. Please install these libraries to continue the real data analysis.")
    exit()

# --- 2. DATA LOADING AND FLATTENING FUNCTION ---

def load_data_from_file(file_path, file_key, max_events):
    """
    Loads specific lepton data (Muon or Electron) based on the trigger file type (file_key).
    Returns a flattened DataFrame for that file.
    """

    # 1. Determine the branches to load based on the trigger type
    if "DoubleMuon" in file_key:
        lepton_prefix = "Muon"  # Capitalized to match branch names
        branches = MUON_BRANCHES
        flavor_pdg = 13 # Muon
    elif "DoubleElectron" in file_key:
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
                entry_stop=max_events,
                library="ak"
            )
            print(f"Step 1: Raw Data read OK")

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

            # Diagnostic
            print(f"Diagnostic: Read {len(raw_data)} events. Number of {lepton_prefix}s in the first event: {lepton_counts_np[0] if len(lepton_counts_np) > 0 else 0}")

            # 2. Flatten the lepton data (pt, eta, phi, etc.)
            # We don't loop because renaming is complex with capitalization.

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
            print(f"Step 2: Flatten OK")

            # --- KEY CORRECTION: ENFORCE NUMERIC TYPING FOR 'VECTOR' ---
            kinematic_cols = ['pt', 'eta', 'phi', 'mass']
            for col in kinematic_cols:
                # Ensure kinematic columns are of standard float64 type
                if col in df.columns:
                    df[col] = df[col].astype(np.float64)

            # Add the flavor identification column (PDG ID)
            df['flavor'] = flavor_pdg
            print(f"Step 3: ID OK")

            for col in kinematic_cols:
                print(f"DEBUG: Type/Dtype of df['{col}'].values: {type(df[col].values)} / {df[col].values.dtype}")

            print(f"Success: {len(df)} leptons loaded from {file_key}.")
            return df

    except Exception as e:
        # Leave a clearer message for the user
        print(f"\nERROR: Could not load file {file_path}. Does the file exist and contain an 'Events' TTree?")
        print(f"Error details: {e}")
        return pd.DataFrame()

def load_and_flatten_data(data_files_map, max_events):
    """
    Loads data from all specified files and concatenates them into one DataFrame.
    """
    all_dfs = []

    print(f"Attempting to load a maximum of {max_events} events per file...")
    for key, file_name in data_files_map.items():
        if os.path.exists(file_name):
            df = load_data_from_file(file_name, key, max_events)
            if not df.empty:
                all_dfs.append(df)
        else:
            print(f"WARNING: File not found '{file_name}'. Skipped. Check the path.")

    if not all_dfs:
        print("Loading failed: No data file was successfully loaded.")
        return pd.DataFrame()

    # Concatenate all loaded DataFrames
    final_df = pd.concat(all_dfs, ignore_index=True)
    print(f"\nTotal loading successful. Total of {len(final_df)} leptons ready for analysis.")
    return final_df

# --- 3. APPLY QUALITY CUTS (Implementation of Roadmap Step) ---

def apply_quality_cuts(df):
    """
    Applies the minimal quality and kinematic cuts to individual leptons.
    This is the first essential filtering step in the H -> 4l analysis.
    """
    initial_count = len(df)

    if initial_count == 0:
        print("The DataFrame is empty, no quality cuts applied.")
        return df

    # A. KINEMATIC CUT ON PT (Transverse Momentum)
    pt_cut = 5.0
    df_pt_filtered = df[df['pt'] > pt_cut]
    print(f"-> pT cut > {pt_cut} GeV: {initial_count - len(df_pt_filtered)} leptons rejected.")

    # B. ACCEPTANCE CUT ON ETA (Pseudorapidity)
    eta_max = 2.5
    df_eta_filtered = df_pt_filtered[np.abs(df_pt_filtered['eta']) < eta_max]
    print(f"-> |eta| cut < {eta_max}: {len(df_pt_filtered) - len(df_eta_filtered)} leptons rejected (after pT).")

    # C. ISOLATION CUT (Rejecting Leptons from Jets)
    iso_cut = 0.3
    df_final = df_eta_filtered[df_eta_filtered['iso'] < iso_cut]
    print(f"-> Isolation Cut (iso < {iso_cut}): {len(df_eta_filtered) - len(df_final)} leptons rejected (after pT and eta).")

    final_count = len(df_final)
    print(f"\nTotal leptons after quality cuts: {final_count}")
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
        print(f"\n--- MASS CORRECTION: {num_neg_mass} negative masses forced to 0.0 ---")
        df.loc[negative_mass_mask, 'mass'] = 0.1

    # 2. CLEANUP: Mask for NaN/Inf (all columns must be finite)
    is_finite = np.all(np.isfinite(df[kinematic_cols].values), axis=1)

    # 3. CLEANUP: Mask for pT > 0 (mass is now >= 0 thanks to step 1)
    pt_ok = df['pt'] > 0

    # Combined mask for valid data that remains inside
    valid_mask = is_finite & pt_ok

    df_cleaned = df[valid_mask].reset_index(drop=True)
    removed_count = initial_count - len(df_cleaned)

    if removed_count > 0:
        print(f"-> Final cleanup after correction: {removed_count} rows rejected (NaN, Inf, or pT <= 0).")
    else:
        print("-> Final cleanup: No invalid data found after mass correction.")

    return df_cleaned


# --- 4. DIAGNOSTICS: PLOT KINEMATIC DISTRIBUTIONS ---

def plot_kinematic_diagnostics(df_before, df_after):
    """
    Plots pT and eta distributions to visualize the effect of the applied cuts.
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # --- Plot pT Distribution ---
    axes[0].hist(df_before['pt'], bins=50, range=(0, 100), histtype='step',
                 label='Before cuts', color='blue', density=True)
    axes[0].hist(df_after['pt'], bins=50, range=(0, 100), histtype='stepfilled', alpha=0.6,
                 label=f'After cuts ({len(df_after)} leptons)', color='red', density=True)

    # Vertical line to show the pT > 5 GeV cut
    axes[0].axvline(5.0, color='red', linestyle='--', linewidth=1, label='$p_T > 5 \\text{ GeV}$')

    axes[0].set_yscale('log')
    axes[0].set_xlabel('$p_T$ of Lepton (GeV)')
    axes[0].set_ylabel('Events (Normalized)')
    axes[0].set_title('$p_T$ Distribution (Transverse Momentum)')
    axes[0].legend()
    axes[0].grid(axis='y', alpha=0.5)

    # --- Plot eta Distribution ---
    axes[1].hist(df_before['eta'], bins=40, range=(-3.0, 3.0), histtype='step',
                 label='Before cuts', color='blue', density=True)
    axes[1].hist(df_after['eta'], bins=40, range=(-3.0, 3.0), histtype='stepfilled', alpha=0.6,
                 label=f'After cuts ({len(df_after)} leptons)', color='red', density=True)

    # Vertical lines to show the |eta| < 2.5 cut
    axes[1].axvline(2.5, color='red', linestyle='--', linewidth=1, label='$|\\eta| < 2.5$')
    axes[1].axvline(-2.5, color='red', linestyle='--', linewidth=1)

    axes[1].set_xlabel('$\\eta$ of Lepton (Pseudorapidity)')
    axes[1].set_ylabel('Events (Normalized)')
    axes[1].set_title('$\\eta$ Distribution (Acceptance)')
    axes[1].legend()
    axes[1].grid(axis='y', alpha=0.5)

    plt.tight_layout()
    plt.show()

# --- 5. MAIN EXECUTION ---
print("--- START OF H -> 4l ANALYSIS (Real Data) ---")

# 1. Load the original data
all_leptons_df_initial = load_and_flatten_data(DATA_FILES, MAX_EVENTS)

if not all_leptons_df_initial.empty:
    # 2. Apply individual quality cuts
    filtered_leptons_df = apply_quality_cuts(all_leptons_df_initial)

    cleaned_leptons_df = clean_kinematic_data(filtered_leptons_df)
    # 4. CREATION OF LORENTZ VECTORS ON ALL FILTERED DATA (The right way)
    print("\nStep 4: Creation of Lorentz Vector (lv) objects on the complete filtered DataFrame...")
    try:
        vector_array_temp = vector.array({
            "pt": cleaned_leptons_df['pt'],
            "eta": cleaned_leptons_df["eta"],
            "phi": cleaned_leptons_df["phi"],
            "mass": cleaned_leptons_df["mass"]
        })

        cleaned_leptons_df['lv'] = vector_array_temp


        print("Success: 'lv' column of Lorentz vectors added to the DataFrame.")
        print(cleaned_leptons_df['lv'].values.dtype)

    except Exception as e:
        print(f"\nCRITICAL ERROR during creation of 'lv' column: {e}")
        print("The analysis cannot continue. Please check the installation or version of 'vector'.")


    # 3. VERIFICATION: Display diagnostics
    plot_kinematic_diagnostics(all_leptons_df_initial, cleaned_leptons_df)

    # 4. Confirm the next step
    print("\n--- STATUS: Quality cuts applied and verified. ---")

    if not cleaned_leptons_df.empty:
        print("\nPreview of filtered leptons (ready for combination):")
        print(cleaned_leptons_df[['event_id', 'pt', 'charge', 'flavor', 'iso']].head())