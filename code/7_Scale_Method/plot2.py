import matplotlib.pyplot as plt
import pandas as pd
import os
import glob

DATA_FILES = {
    #"DoubleMuon_B": "../../data/12365/Run2012B_DoubleMuParked.root",
    "DoubleMuon_C": "../../data/12366/Run2012C_DoubleMuParked.root",
    "DoubleElectron_B": "../../data/12367/Run2012B_DoubleElectron.root",
    "DoubleElectron_C": "../../data/12368/Run2012C_DoubleElectron.root"
}

BASE_CHUNK = "../../data/"

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
