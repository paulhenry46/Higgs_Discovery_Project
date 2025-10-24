# Methodology of detection
##  General Principles of Particle Detection in High-Energy Physics

The Higgs boson, like all other short-lived, massive particles (such as the $Z$ and $W$ bosons), cannot be observed directly. It decays almost instantaneously into lighter, stable particles. Therefore, according to [^CERN_1], the general methodology for detection involves a three-step process: **Creation**, **Decay**, and **Reconstruction**.

### I. Creation: The Accelerator (LHC)

Detection starts with the creation of the desired particle in a high-energy collision.

1.  **Acceleration:** Charged particles (protons at the LHC) are accelerated by powerful **electromagnetic fields** to speeds approaching the speed of light ($0.99999999 c$).
2.  **Collision:** These particle beams are then brought into head-on collision. According to Einstein’s equation $E=mc^2$, the high **kinetic energy** of the colliding protons is converted into **mass**, momentarily creating heavy particles like the Higgs boson ($H$), which existed only for a fleeting moment in the early universe.

### II. Detection: The Particle Detector (CMS/ATLAS)

The detector is a massive, multi-layered instrument designed to capture the properties of the stable decay products.

| Detector Layer | Function | Measurable Property |
| :--- | :--- | :--- |
| **1. Tracking Chamber** (Inner Layer) | Measures the path of electrically charged particles. | **Trajectory, Momentum, Charge Sign.** The path is curved by a strong magnetic field, allowing momentum ($p$) to be calculated from the curvature. |
| **2. Calorimeters** (Middle Layers) | Measures the total energy of particles by forcing them to stop. | **Energy ($E$).** Separated into: **Electromagnetic Calorimeter** (measures electrons and photons) and **Hadronic Calorimeter** (measures hadrons). |
| **3. Muon Chambers** (Outer Layer) | Detects particles that pass through all other layers. | **Muons** (as they interact weakly). **Neutrinos** pass through completely and are detected only by missing momentum. |

### III. Identification and Reconstruction

The signals from the different detector layers combine to create a **"particle signature"**, allowing physicists to identify the particle type and ultimately reconstruct the event.

1.  **Particle Signatures:** Each type of stable particle leaves a unique signature:
    * **Electrons ($e$)**: Track in the inner layer, absorbed fully in the Electromagnetic Calorimeter.
    * **Photons ($\gamma$)**: No track (neutral), absorbed fully in the Electromagnetic Calorimeter.
    * **Muons ($\mu$)**: Track in the inner layer, only leaves a trace in the Muon Chambers.
    * **Neutrinos ($\nu$)**: No signature. Their presence is inferred from the **Missing Transverse Energy ($E_T^{\text{miss}}$)** required to conserve momentum.
    * **Jets (Quarks/Gluons)**: Broad cone of energy deposits in the Hadronic Calorimeter, caused by a cascade of strongly interacting particles.

2.  **The Role of Four-Momentum:** The measured momentum ($\vec{p}$) and energy ($E$) of the decay products are combined into their **Four-Momentum** ($P = (E, \vec{p})$).

3.  **Reconstruction (Invariant Mass):** The four-momenta of all final decay products are summed up. The resulting invariant mass of the system must equal the mass of the parent particle that decayed.
    $$\mathbf{M_{\text{parent}}^2 = \left(\sum E_i\right)^2 - \left|\sum \vec{p}_i\right|^2}$$

This general process establishes that **discovery is always indirect**, based on reconstructing the properties of an unobserved, short-lived parent particle from the measured properties of its stable children.
## Decay Channel

A **Decay Channel**  refers to a specific set of stable particles that an unstable, high-mass particle (the parent) can transform into.

In quantum mechanics, a massive particle's existence is fleeting. It spontaneously converts its mass-energy ($E=mc^2$) into kinetic energy and the mass of lighter particles, governed by the laws of conservation (energy, momentum, charge, etc.).

A given parent particle may have several possible decay channels, each associated with a unique **Branching Ratio** ($BR$) which is the probability that the particle will take that specific path.

### 1. Nomenclature and the Higgs Boson ($H$)

A decay channel is defined by its initial state (the parent) and its final, stable decay products.

For the Higgs boson, with a mass of $M_H \approx 125 \text{ GeV/c}^2$, the selection of channels is governed by the **mass proportionality principle** : the Higgs prefers to couple to and decay into the heaviest particles kinematically allowed (i.e. if coumpling respect the conservatives laws).

| Channel Name | Decay Process | Branching Ratio (BR) at $125 \text{ GeV/c}^2$ | Why this BR? |
| :--- | :--- | :--- | :--- |
| **Most Probable** | $H \rightarrow b\bar{b}$ | $\sim 58 \%$ | Highest BR due to the strong **Yukawa coupling** to the heavy bottom quark ($b$). |
| **Second Most Probable** | $H \rightarrow W^+ W^-$ | $\sim 21 \%$ | Strong coupling to the massive $W$ bosons. |
| **Golden Channel** | $H \rightarrow Z Z \rightarrow 4\ell$ | $\sim 0.012 \%$ | Very low BR, as it requires two massive $Z$ bosons, followed by $Z \rightarrow e^+e^-$ or $Z \rightarrow \mu^+\mu^-$. |

The remaining ∼21% is distributed among other physically possible decay channels predicted by the Standard Model.

### 2. How to determine all possibles paths ?

The process of determining which decay channels are physically possible involves two steps: first, establishing that the path is kinematically allowed by conservation laws, and second, calculating its probability using Quantum Field Theory.

#### Step 1: Establishing Possibility (Conservation Laws)

A decay path is only possible if it respects all known fundamental conservation laws. If a decay violates even one of these laws, its probability is strictly zero.

| Conservation Law | Physical Requirement | Example |
| :--- | :--- | :--- |
| **Energy/Momentum** ($\mathbf{P}$) | The energy and momentum of the parent particle must equal the sum of the energy and momentum of all decay products. This is ensured by the **Four-Momentum** formalism. | A decay of a low-mass particle into products whose **total mass is greater** than the parent's mass ($\mathbf{M}_{\text{parent}} < \sum \mathbf{M}_{\text{products}}$). |
| **Electric Charge** ($Q$) | The total electric charge must be conserved. | A neutral particle (like the $Z$ boson, $Q=0$) decaying into products with a non-zero net charge (e.g., $Z \rightarrow e^+ + \mu^{-}$ is allowed) |
| **Lepton & Baryon Number** ($L, B$) | The total number of leptons and baryons must remain the same. This prevents a muon ($\mu^-$) from decaying directly into a single electron ($e^-$). | $\mu^{-} \rightarrow e^{-}$ (Violates Lepton Number conservation). The correct path is $\mu^{-} \rightarrow e^{-} + \nu_{\mu} + \bar{\nu}_{e}$. |
| **Angular Momentum (Spin)** | The total angular momentum (including spin) must be conserved during the decay. | Crucial for the Higgs Boson (spin 0), whose decay products' spins must sum to zero. |

 Any channel that passes all conservation checks is considered **kinematically allowed**.

#### Step 2: Calculating Probability (Feynman Diagrams)

Once a path is determined to be possible, its relative probability, or **Branching Ratio ($BR$)**, is calculated using **Quantum Field Theory (QFT)**, specifically through **Feynman Diagrams**.

A Feynman diagram is a pictorial representation of an interaction. Every line (representing a particle) and every vertex (representing an interaction point) corresponds to a mathematical term in the full QFT calculation. 

1.  **Drawing the Diagrams:** For a given initial state (e.g., a Higgs Boson, $H$) and a final state (e.g., a bottom-antibottom quark pair, $b\bar{b}$), physicists draw all possible Feynman diagrams that connect the two states.
2.  **Assigning Amplitudes:** A mathematical expression called an **amplitude** is assigned to each diagram. The final amplitude is a summation over all possible diagrams, and the decay rate is proportional to the square of this amplitude.
3.  **The Role of Coupling Constants:** The amplitude is heavily dependent on the **coupling constants** at the vertices.
    * For the Higgs decay, the amplitude is proportional to the **Yukawa Coupling ($g_f$)** for decays into fermions (like $H \rightarrow b\bar{b}$) or the gauge couplings for decays into bosons (like $H \rightarrow Z Z$).
    * **The Larger the Coupling Constant, the Higher the Probability.** This is why $H \rightarrow b\bar{b}$ (high Yukawa coupling) is highly probable, and $H \rightarrow 4\ell$ (low effective coupling) is rare.

### Final Calculation: The Branching Ratio

The overall decay probability for a specific channel is summarized by the **Branching Ratio ($BR$):**

$$\mathbf{BR}(\text{Channel } X) = \frac{\text{Decay Rate of Channel } X \text{ ($\Gamma_X$)}}{\text{Total Decay Rate (Sum of all) } \Gamma_i}$$

This calculation, derived from the sum of all relevant Feynman diagrams, allows us to predict the $BR$ values  before the particle is observed in the detector.

<!-- Exemple of calculation for a BR + Source -->

### 3. Experimental Selection Criteria

In experimental particle physics, the selection of a decay channel is a compromise between the theoretical probability ($BR$) and the practicality of detection, known as the **Signal-to-Background Ratio**.

| Channel Type | Characteristic | Detection Challenge |
| :--- | :--- | :--- |
| **High BR** ($H \rightarrow b\bar{b}$) | **High Signal, High Background** | The final particles ($b$ quarks) fragment into **jets** of hadrons, which are nearly indistinguishable from the "junk" produced by standard proton-proton collisions. This leads to a very poor signal-to-background ratio. |
| **Low BR** ($H \rightarrow 4\ell$) | **Low Signal, Very Low Background** | The final particles are **leptons** (electrons $e$ and muons $\mu$), which pass cleanly through the detector layers, leaving distinct and isolated signatures. This leads to an extremely high (clean) signal-to-background ratio. |

## The Golden Channel

The **Golden Channel** refers to the decay path of the Higgs boson ($H$) into four charged leptons (electrons $e^{\pm}$ or muons $\mu^{\pm}$), denoted as $H \rightarrow Z Z \rightarrow 4\ell$. This channel was crucial for the 2012 discovery due to its exceptionally **clean signature** despite its rarity.

### 1. Kinetic Possibility (Feasibility Check)

A decay channel is kinematically possible if the mass of the parent particle is greater than or equal to the sum of the masses of its final, stable products.

For the Golden Channel, the decay chain is:

$$\mathbf{H} \longrightarrow \mathbf{Z} + \mathbf{Z} \longrightarrow (\ell_1^+ + \ell_1^-) + (\ell_2^+ + \ell_2^-)$$

We must check the initial decay of the Higgs into two $Z$ bosons.

| Particle | Standard Model Mass ($M$) |
| :--- | :--- |
| **Higgs Boson ($H$)** | $M_H \approx 125 \text{ GeV/c}^2$ (Observed Mass) |
| **$Z$ Boson ($Z$)** | $M_Z \approx 91.2 \text{ GeV/c}^2$ |

**The Kinematic Problem:**

$$M_H \quad \mathbf{vs} \quad M_Z + M_Z$$
$$125 \text{ GeV/c}^2 \quad \mathbf{vs} \quad 91.2 \text{ GeV/c}^2 + 91.2 \text{ GeV/c}^2 = \mathbf{182.4 \text{ GeV/c}^2}$$

Since $125 \text{ GeV/c}^2 < 182.4 \text{ GeV/c}^2$, the decay of the Higgs into two **on-shell** (real, fully massive) $Z$ bosons is **kinetically forbidden**.

**The Solution :**

The channel is saved by **Quantum Mechanics**. One or both of the $Z$ bosons produced by the Higgs must be virtual. A virtual particle is a temporary fluctuation that does not respect the mass-shell constraint ($M=91.2 \text{ GeV/c}^2$), allowing it to have a lower mass.

The decay is therefore correctly written as:

$$\mathbf{H} \longrightarrow \mathbf{Z} + \mathbf{Z}^{*} \longrightarrow 4\ell$$

Where $\mathbf{Z}^{*}$ represents the virtual $Z$ boson. This allows the total mass of the products to respect the $\mathbf{125 \text{ GeV/c}^2}$ limit, making the decay **kinetically possible**.

***

### 2. Probability (The Rarity of the Channel)

The probability of the Golden Channel is determined by two successive steps, resulting in an overall low **Branching Ratio ($BR$)**:

#### A. $H \rightarrow Z Z$ Probability (Coupling)

The $H \rightarrow Z Z$ decay is the result of the Higgs coupling to the massive gauge bosons. This coupling is strong (proportional to $M_Z^2 / v$), which makes $H \rightarrow Z Z$ a **relatively high** BR channel compared to others like $H \rightarrow \gamma \gamma$.

However, because one of the $Z$ bosons must be **virtual** ($\mathbf{Z}^{*}$), the decay rate is significantly suppressed compared to if both were real. Indeed, the more virtual the particle is (the further it is from its actual mass MZ), the lower the probability of its existence and decay. This virtual suppression keeps the $H \rightarrow Z Z$ BR at $\sim 2.7\%$ according to [^CERN_2].

#### B. $Z \rightarrow \ell^+ \ell^-$ Probability (The Filter)

For the final state to be **clean** ($4\ell$), each $Z$ boson (or $Z^{*}$) must decay into a pair of charged leptons ($e^+e^-$ or $\mu^+\mu^-$).

The probability of a single $Z$ boson decaying into charged leptons is, according to [^Particle_Review] 
$$BR(Z \rightarrow \ell^+\ell^-) \approx \mathbf{3.36\%}$$

#### C. Final Branching Ratio Calculation

Since both $Z$ bosons must decay into charged leptons, the overall BR is the product of the probabilities:

$$\mathbf{BR}(H \rightarrow 4\ell) = BR(H \rightarrow Z Z) \times BR(Z \rightarrow \ell^+\ell^-) \times BR(Z \rightarrow \ell^+\ell^-)$$

$$\mathbf{BR}(H \rightarrow 4\ell) \approx 0.027 \times 0.0336 \times 0.0336 \approx \mathbf{0.00003} \quad \text{or} \quad \mathbf{0.003 \%}$$

*(Note: The actual observed BR, factoring in all final lepton combinations, is $\mathbf{\sim 0.012\%}$)*.

The key conclusion is that the $H \rightarrow Z Z \rightarrow 4\ell$ channel is **possible** through virtual particles, but its probability is extremely **low** due to the requirement that both $Z$ bosons must decay into leptons. This rarity is a worthwhile sacrifice for its **unambiguous, clean signal** in the detector.

[^CERN_1]: CERN Documentation on Detectors https://home.cern/science/experiments/how-detector-works

[^CERN_2] : https://arxiv.org/pdf/1101.0593 (Branching ration table 28)

[^Particle_Review] https://pdg.lbl.gov/2020/tables/rpp2020-sum-gauge-higgs-bosons.pdf page 3