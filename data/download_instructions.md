# Create Python env
python3 -m venv higgs_env
source higgs_env/bin/activate

pip install requirements.txt
# Download and set up Root
Root enable to read the .root files we will download. You can get  at [the ROOT homepage](https://root.cern/install/#download-a-pre-compiled-binary-distribution)

In my case, because I use a debian based distribution and because i don't want to use snap, i choose to install from the binary method. If you do the same, don't forget to add `source /path/to/root/bin/thisroot.sh` at the end of `higgs_env/bin/activate` file we create above.

You can check if it is installed and ready by running the `text.py` file.

# Download Data
## With HTTP
This way is not advices, since you can experiment errors because CERN servers can produce timeout or gateway error.
We will use the files provided by the CERN in [this record](https://opendata.cern.ch/record/12360) :
- [SMHiggsToZZTo4L.root](https://opendata.cern.ch/record/12361/files/SMHiggsToZZTo4L.root)
- [ZZTo4mu.root](https://opendata.cern.ch/record/12362/files/ZZTo4mu.root)
- [ZZTo4e.root](https://opendata.cern.ch/record/12363/files/ZZTo4e.root)
- [ZZTo2e2mu.root](https://opendata.cern.ch/record/12364/files/ZZTo2e2mu.root)
- [Run2012B_DoubleMuParked.root](https://opendata.cern.ch/record/12365/files/Run2012B_DoubleMuParked.root) (3 Gib)
- [Run2012C_DoubleMuParked.root](https://opendata.cern.ch/record/12366/files/Run2012C_DoubleMuParked.root) (4 Gib)
- [Run2012B_DoubleElectron.root](https://opendata.cern.ch/record/12367/files/Run2012B_DoubleElectron.root) (1.7 Gib)
- [Run2012C_DoubleElectron.root](https://opendata.cern.ch/record/12368/files/Run2012C_DoubleElectron.root) (2.6 GiB)

## With the CERN Client
Run `pip install cernopendata-client` The dependency is not included in requirements.txt because it is not strcyly mandatory.

Run `cernopendata-client download-files --recid 12361` or for better performances `cernopendata-client download-files --recid 12361 --protocol xrootd` and repeat for records `12362 12363 12364 12365 12366 12367 12368`.
### Script
You can also use the script `download_script.sh` to download all files with `xrootd` protocol.
### XRoot Protocol
If you want to use XRoot Protocol, you will need to install it : `sudo apt install xrootd-client`

We will see what these data correspond to in another section.

# Explanation of downloaded files

The datasets are divided into two categories: **Real Collision Data** (Observation) and **Simulated Data** (Templates).

## 1. Real Collision Data

These files contain the actual physics events recorded by the CMS detector in 2012. The Higgs signal is contained within these files, mixed with all known backgrounds.

| Dataset Name | Final State Coverage | Rationale |
| :--- | :--- | :--- |
| **`Run2012B_DoubleMuParked`** |  $4\mu$, $2e2\mu$ | Data triggered by two muons. Essential to observe the $4\mu$ channel and partially the $2e2\mu$ channel. |
| **`Run2012C_DoubleMuParked`** |  $4\mu$, $2e2\mu$ | Complements Run B data to increase the total number of events (luminosity), improving statistical certainty. |
| **`Run2012B_DoubleElectron`** |  $4e$, $2e2\mu$ | Data triggered by two electrons. Essential to observe the $4e$ channel and partially the $2e2\mu$ channel. |
| **`Run2012C_DoubleElectron`** |  $4e$, $2e2\mu$ | Complements Run B data for electron triggers. **All four** Run 2012 files are needed for the full $H \rightarrow 4\ell$ analysis. |

---

## 2. Monte Carlo (MC) Simulation Data

These files are computer-generated events based on theoretical models. They are used to **model** the shape of the signal and accurately **subtract** the background noise.

### A. Background Templates (The Noise Model)

The primary background that fakes the $H \rightarrow 4\ell$ signal is the direct production of two $Z$ bosons ($Z Z$).

| Dataset Name | Final State | Rationale |
| :--- | :--- | :--- |
| **`ZZTo4mu dataset`** |  $Z Z \rightarrow 4\mu$ | Used to model the **$4\mu$ background** shape, allowing for accurate subtraction from the real data in this specific channel. |
| **`ZZTo4e dataset`** |  $Z Z \rightarrow 4e$ | Used to model the **$4e$ background** shape. |
| **`ZZTo2e2mu dataset`** |  $Z Z \rightarrow 2e2\mu$ | Used to model the **$2e2\mu$ background** shape. |

### B. Signal Template (The Target Model)
It will be only used to validate and quantify our results.

| Dataset Name | Final State | Rationale |
| :--- | :--- | :--- |
| **`SMHiggsToZZTo4L dataset`** | All $4\ell$ | Provides the **ideal, theoretical shape** of the Higgs peak at $125 \text{ GeV/c}^2$. Used to perform a statistical fit and constrain the final mass measurement. |