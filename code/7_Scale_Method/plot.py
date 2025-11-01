import matplotlib.pyplot as plt
import pandas as pd
import os
import glob

DATA_FILES = {
    "DoubleMuon_B": "../../data/12365/Run2012B_DoubleMuParked.root",
    "DoubleMuon_C": "../../data/12366/Run2012C_DoubleMuParked.root",
    "DoubleElectron_B": "../../data/12367/Run2012B_DoubleElectron.root",
    "DoubleElectron_C": "../../data/12368/Run2012C_DoubleElectron.root"
}

BASE_CHUNK = "../../data/"


def plot_higgs_mass(z_boson_df):
    """ Displays the final invariant mass M4l distribution. """
    
    # Check if the DataFrame is empty before attempting to plot
    if z_boson_df.empty:
        print("DEBUG: Z candidate DataFrame is empty; cannot plot Higgs mass.")
        return
        
    print("\n--- STATUS: Z Candidates and Higgs Mass ($M_{4l}$) calculated. ---")
    # Display the histogram of the Higgs invariant mass
    plt.figure(figsize=(10, 6))
    plt.hist(
        z_boson_df['mass'], 
        bins=20, 
        range=(80, 150), 
        color='skyblue', 
        edgecolor='black', 
        alpha=0.7, 
        label='$M_{4\ell}$ Distribution'
    )
    
    # Reference line for the known Higgs mass (125 GeV)
    plt.axvline(125.09, color='red', linestyle='--', linewidth=2, label='$M_H \\approx 125.1$ GeV') 

    plt.title('Invariant Mass Distribution $M_{4\ell}$ (Higgs Candidates)')
    plt.xlabel('Invariant Mass $M_{4\ell}$ (GeV)')
    plt.ylabel("Number of Events")
    plt.legend()
    plt.grid(axis='y', alpha=0.5)
    plt.show() 

    print(f"\nHiggs invariant mass (M_4l) histogram generated for {len(z_boson_df)} events.")

def load_csv_folder(folder_path, pattern="*.csv", usecols=None, dtype=None,
                    parse_dates=None, chunksize=None):
    """
    Load many CSV files from a folder into a single pandas DataFrame.

    Parameters:
    - folder_path: path to the folder containing CSV files
    - pattern: glob pattern (default: '*.csv')
    - usecols, dtype, parse_dates: forwarded to pandas.read_csv
    - chunksize: if set, will use pandas.read_csv(..., chunksize=...) and concatenate chunks

    Returns:
    - concatenated pandas.DataFrame
    """
    files = sorted(glob.glob(os.path.join(folder_path, pattern)))
    if not files:
        raise FileNotFoundError(f"No files found in {folder_path} matching {pattern}")

    frames = []
    for f in files:
        if chunksize:
            for chunk in pd.read_csv(f, usecols=usecols, dtype=dtype,
                                     parse_dates=parse_dates, chunksize=chunksize):
                frames.append(chunk)
        else:
            df = pd.read_csv(f, usecols=usecols, dtype=dtype, parse_dates=parse_dates)
            frames.append(df)

    result = pd.concat(frames, ignore_index=True)
    return result

z_df = load_csv_folder(BASE_CHUNK)

plot_higgs_mass(z_df)