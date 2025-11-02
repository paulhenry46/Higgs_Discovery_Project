# Finding the Higgs Boson in the Four-Lepton Channel

This repository contains the analysis script used to search for the Higgs Boson ($H$) using real data from the CMS experiment at the Large Hadron Collider (LHC).

Our goal is to find the extremely rare signature where the Higgs instantly decays into two Z particles, which then immediately decay into four final, easily detectable leptons (electrons and muons).

## 🔍 The Scientific Goal

The Higgs Boson is known to have a mass of approximately **$125\ \text{GeV}$**.

When we reconstruct the Higgs through this decay, we expect the total mass of the four final particles ($M_{4\ell}$) to be exactly that value.

The core challenge of this project is to use a sequence of powerful filters and cuts to remove overwhelming background noise and reveal this tiny **$125\ \text{GeV}$ peak** in the mass spectrum.
## 🛠️ How the Search Works

The analysis follows three main steps to reconstruct the event and eliminate backgrounds:

### 1. Identify "Golden" Leptons
We first filter the raw collision data to keep only the best, high-quality light particles (leptons). We reject those that are too low in energy or don't seem to originate from the main collision point.

### 2. Reconstruct the $Z$ Particles
We take the four remaining "golden" leptons and try to pair them up to form two intermediate particles: $\text{Z}_1$ and $\text{Z}_2$.

* **The $Z_1$** is the pair whose combined mass is closest to the official $Z$ boson mass ($91\ \text{GeV}$).
* **The $Z_2$** is formed by the two remaining leptons.

### 3. Comparing with Monte Carlo Simulation
To confirm the discovery, we compare the data with Monte Carlo simulations of background noise and the Higgs signal.

## ⚙️ Technical Details
The analysis is divided into several Jupyter notebooks. It uses the `awkward`, `uproot`, and `pandas` libraries. We do not vectorize the functions in order to better understand the physics behind them. This is a demonstration, so performance is not important.

## 📑 Available Documents:
Placed in recommended reading order to fully understand the project and the physics behind it :
- [Maths & kinematics reference (`docs/maths_utils.md`)](docs/maths_utils.md) — Quantum Field Theory reminders, four-momentum and invariant mass used in reconstruction.
- [Theory (`docs/theory.md`)](docs/theory.md) — Standard Model, BEH mechanism and Higgs properties.
- [Methodology (`docs/methodology.md`)](docs/methodology.md) — Detection strategy, event selection and invariant mass reconstruction for the golden channel.
- [Data download & setup (`data/download_instructions.md`)](data/download_instructions.md) — Environment setup and links to the CERN open data files used.
- [Dependencies (`requirements.txt`)](requirements.txt) — Python packages needed to run the analysis.

## 💼 Project Structure
- data/ — raw input files and download instructions ([data/download_instructions.md](data/download_instructions.md))
- code/ — analysis scripts and notebooks
- plots/ — generated figures
- docs/ — documentation