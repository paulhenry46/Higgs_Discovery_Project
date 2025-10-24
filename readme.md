#### Higgs Project

A compact analysis project to study the Higgs boson in the golden channel (H → ZZ → 4ℓ) using CERN open data. The repository collects the theory background, analysis methodology, maths references and data download/setup instructions required to reproduce the work.

Overview of docs documents:
- [Maths & kinematics reference (`docs/maths_utils.md`)](docs/maths_utils.md) — Quantum Field Theory reminders, four-momentum and invariant mass used in reconstruction.
- [Theory (`docs/theory.md`)](docs/theory.md) — Standard Model, BEH mechanism and Higgs properties.
- [Methodology (`docs/methodology.md`)](docs/methodology.md) — Detection strategy, event selection and invariant mass reconstruction for the golden channel.
- [Data download & setup (`data/download_instructions.md`)](data/download_instructions.md) — Environment setup and links to the CERN open data files used.
- [Dependencies (`requirements.txt`)](requirements.txt) — Python packages needed to run the analysis.

Quick start:
1. Create and activate a Python virtual environment as described in [data/download_instructions.md](data/download_instructions.md).
2. Install dependencies from [requirements.txt](requirements.txt).
3. Download the datasets listed in [data/download_instructions.md](data/download_instructions.md) into the `data/` folder.
4. Follow the analysis steps and refer to [docs/maths_utils.md](docs/maths_utils.md) and [docs/methodology.md](docs/methodology.md) for formulas and selection criteria and to [docs/theory.md] for physics understanding of the discovery.

Project layout:
- data/ — raw input files and download instructions ([data/download_instructions.md](data/download_instructions.md))
- code/ — analysis scripts and notebooks
- plots/ — generated figures
- docs/ — documentation