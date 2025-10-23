# Theory
## Standard Model
SRC : https://home.cern/science/physics/standard-model

The Standard Model (SM) of particle physics is the most comprehensive theory describing the fundamental building blocks of the universe and three of the four fundamental forces (electromagnetism, strong and weak nuclear forces) they interact with. It is not a "Theory of Everything" because it notably excludes gravity.
### Fundamental Particles
The Standard Model classifies all known fundamental particles into two groups: Fermions (the matter constituents) and Bosons (the force carriers).
#### Fermions
Fermions are the particles that make up all visible matter. There are 12 types, arranged in three generations. Ordinary matter is made only of the first generation.
##### 1st generation
The Quarks are make up by the Up (u) and Down (d). They combine to form protons (uud) and neutrons (udd) and are affected by the strong force.
For the Leptons, we find the famous electron (e) and Electron Neutrino $\nu_e$​. They are sensitive to the electromagnetic and weak forces, but not the strong force.
#### Other Generations
Thoses partcles are heavier copies which quickly decay of the first generation particles.
#### Bosons
We find the photon $\gamma$, the W and Z Bosons (responsible for radioactive decay), the Gluons (g) (responsible for the Strong force) and of course the Higgs Boson, that interests us.
### Spin
#### Definition
The spin of a particle is an intrinsic form of angular momentum. It is an inherent property of the particle, much like its mass or electric charge. It does not come from the particle moving in space.
#### Direction
The spin value dictates how many spatial orientations a particle can have:

- Spin J=1 : Particles like the photon and W/Z bosons are associated with vector fields. They can have three physical polarization states (degrees of freedom), corresponding to the three spatial directions.
- Spin J=0 : A scalar field (like the Higgs field) is defined by its magnitude only, which has no directional dependence. Therefore, its corresponding particle, the Higgs Boson, must have only one internal degree of freedom, corresponding to zero spin.
### Limits
Despite its accuracy, the Standard Model is incomplete, failing to explain several phenomena, like the gravity (it does not include the gravitational force or its hypothesized carrier, the graviton) and the dark Matter. Indeed,  the SM particles account for only about 5% of the universe's mass-energy. The nature of Dark Matter (about 27%)[S. F. Novaes (2000), table 2, given by $\omega_b, \omega_c$] is completely unknown.
###  Quantum Scalar Field
A Quantum Scalar Field is a fundamental concept in Quantum Field Theory. It allow ue to describe the Standard Model of particle physics. It combines three distinct ideas: Field, Quantum, and Scalar.
#### Field
A field is a physical quantity that has a value at every point in space and time. Instead of thinking of particles as tiny balls, QFT views particles as excitations or vibrations of these omnipresent fields.
#### Quantum 
The term quantum  means the field is governed by the laws of quantum mechanics :

The energy of the field's vibrations can only occur in discrete packets (quanta), not continuously.

Here, the Higgs Boson is the specific quantum (the particle) of the Higgs Field.
#### Scalar
Scalar describes the field's fundamental property: how it behaves when you rotate the space around it.

Definition: A scalar quantity is defined by its magnitude (value) only, and has no direction in space. It's represented by a single number at every point (like temperature).

On the contrary, a Vector Field (like the electromagnetic field) has both magnitude and direction.

Because the Higgs Field is scalar, its corresponding particle, the Higgs Boson, must have zero spin. This is a key experimental confirmation that distinguishes the Higgs from all force-carrying bosons, which have spin J=1.
## Brout-Englert-Higgs (BEH) Mechanism
### Physical View
#### Problem
##### Introduction
The BEH mechanism was required because of a fundamental conflict in physics :
- To successfully unify the electromagnetic and weak nuclear forces into the Electroweak Theory, the theory required the force carriers (W and Z bosons) to be massless.
-  Experiments showed that the W and Z bosons are, in fact, incredibly massive (≈80−91 GeV/c2), and all matter particles also have mass.
##### Gauge Invariance
Simply adding mass terms "by hand" to the equations in the Standard Model's Electroweak Theory would break the underlying symmetry because it violates the principle of Gauge Invariance [Griffiths, Chap. 9-10], which is essential for mathematical consistency and renormalization.

We demonstrate this using the simplest case: a massive gauge field $A_\mu$ (like the photon field in Quantum Electrodynamics, QED, governed by $U(1)$ symmetry). The principle holds for the $W$ and $Z$ bosons.

###### The Gauge Transformation

A gauge transformation [S. F. Novaes, 1.2.1] for a massless field $A_\mu$ (the photon field) is defined by a local shift involving an arbitrary function $\Lambda(x)$ that depends on spacetime $x$:

$$A_\mu(x) \longrightarrow A'_\mu(x) = A_\mu(x) + \partial_\mu \Lambda(x)$$

The kinetic term of the Lagrangian, $\mathcal{L}_{\text{kinetic}} = -\frac{1}{4} F^{\mu\nu} F_{\mu\nu}$, stays the same under this transformation, which preserves Gauge Invariance.

#####  Inserting the "By Hand" Mass Term

To make the gauge boson massive, we attempt to insert the standard QFT mass term structure into the Lagrangian:

$$\mathcal{L}_{\text{mass}} = \frac{1}{2} M^2 A^\mu A_\mu$$

The total Lagrangian would then be:

$$\mathcal{L}_{\text{total}} = -\frac{1}{4} F^{\mu\nu} F_{\mu\nu} + \frac{1}{2} M^2 A^\mu A_\mu$$

##### Testing the Gauge Invariance of the Mass Term

We apply the gauge transformation  only to the mass term $\mathcal{L}_{\text{mass}}$ to see if it remains unchanged:

$$\mathcal{L}'_{\text{mass}} = \frac{1}{2} M^2 A'^\mu A'_\mu$$

Substituting $A'_\mu(x)$:

$$\mathcal{L}'_{\text{mass}} = \frac{1}{2} M^2 (A^\mu + \partial^\mu \Lambda) (A_\mu + \partial_\mu \Lambda)$$

Expanding the terms gives:

$$\mathcal{L}'_{\text{mass}} = \frac{1}{2} M^2 (A^\mu A_\mu + 2 A^\mu \partial_\mu \Lambda + (\partial^\mu \Lambda) (\partial_\mu \Lambda))$$

Separating the original mass term from the new terms:

$$\mathcal{L}'_{\text{mass}} = \mathcal{L}_{\text{mass}} + \mathbf{M^2 A^\mu \partial_\mu \Lambda} + \mathbf{\frac{1}{2} M^2 (\partial^\mu \Lambda) (\partial_\mu \Lambda)}$$

##### Conclusion: The Violation

Because the two  terms  do not cancel out, the Lagrangian **changes** under the gauge transformation:

$$\mathcal{L}'_{\text{mass}} \neq \mathcal{L}_{\text{mass}}$$

The explicit mass term $\mathcal{L}_{\text{mass}} = \frac{1}{2} M^2 A^\mu A_\mu$ **violates Gauge Invariance**.
#### Spontaneous Symmetry Breaking
##### Symetry Breaking
The BEH mechanism resolves our issue by introducing the Higgs Field which permeates all of space.

The Higgs Field possesses a unique energy configuration, mathematically described by the "Mexican Hat Potential".Due to the shape of this potential, the state of lowest energy - Vacuum Expectation Value (VEV) -  is not zero ($v\neq 0$). Instead, the field spontaneously settles on a constant, non-zero value (v≈246 GeV) everywhere in space. This phenomena is called Spontaneous Symmetry Breaking (SSB).

##### Mass Acquisition
The VEV (v) of the Higgs Field is what gives mass to other particles:
- For W and Z Bosons: These force carriers interact strongly with the VEV of the Higgs Field. This interaction effectively "drags" on them, giving them their large masses. The photon (γ), which does not interact with the Higgs Field, remains massless. The other acquire mass proportional to $v^2$.
- For Fermions: They acquire mass through a separate interaction called Yukawa Coupling, which links them to the Higgs Field. They acquire mass proportional to $v$.
#### Consequence : The Higgs Boson
The BEH mechanism also predicts the existence of a new particle: the Higgs Boson (H).

The Higgs Boson is simply the quantum excitation of the Higgs Field itself.
### Mathematical Model
#### The Higgs Potential (The "Mexican Hat")

The theory starts with the potential energy term, $V(\Phi)$, from the Higgs Lagrangian [Peskin & Schroeder, Chap. 20]:

$$V(\Phi) = \mu^2 |\Phi|^2 + \lambda |\Phi|^4$$

The necessary conditions for the BEH mechanism are imposed on the constants:
* $\mu^2 < 0$: The term $μ^2∣Φ∣^2$ is negative, causing the potential to "dip down" below zero as you move away from ∣Φ∣=0. The origin ∣Φ∣=0 becomes a local maximum (the peak of the "hat").
* $\lambda > 0$: Ensures the potential is stable (bounded from below). This means there is a well-defined global minimum (the bottom of the "Mexican Hat"). On the contrary, if $\lambda \leq 0$ The potential would fall indefinitely (since the ∣Φ∣4 term is the highest power) and the system would be unstable.

### 2. Finding the Vacuum Expectation Value (VEV)

The stable vacuum state is found by minimizing $V(\Phi)$ with respect to $|\Phi|$:

$$\frac{\partial V}{\partial |\Phi|} = 2 \mu^2 |\Phi| + 4 \lambda |\Phi|^3 = 0$$

Factoring out $|\Phi|$:

$$|\Phi| (2 \mu^2 + 4 \lambda |\Phi|^2) = 0$$

This gives two solutions:

∣Φ∣=0. This is the maximum of the potential (the top of the "hat"). It is not the stable vacuum.

The solution corresponding to the stable minimum (the True Vacuum) is:

$$2 \mu^2 + 4 \lambda |\Phi|^2 = 0$$

Solving for $|\Phi|^2$ gives the square of the VEV :

$$|\Phi|^2 = v^2 = -\frac{\mu^2}{2 \lambda}$$

The VEV itself is:

$$\mathbf{v = |\Phi|_{\text{minimum}} = \sqrt{-\frac{\mu^2}{2 \lambda}}}$$

Since $v$ is non-zero, the field has a constant background value everywhere, which results in Spontaneous Symmetry Breaking (SSB) [Griffiths, Chap. 12].

Indeed, The Higgs Lagrangian, is symmetric under rotations ; the potential $V(Φ)=μ^2∣Φ∣2+λ∣Φ∣4$ is symmetric.

SSB occurs when the physical system settles into a single ground state (the vacuum) that is not symmetric, even though the laws governing the system (the Lagrangian) are symmetric.

If the minimum were at ∣Φ∣=0, the system would respect the full symmetry. But Since the true minimum is on the circle defined by $v \neq 0$​​, the Higgs Field must spontaneously choose a specific point on that circle to settle down to. The physics is the same at any point on the circle, but, by settling at a specific, non-zero point, the vacuum has broken the rotational symmetry of the "hat."

### 3. Finding the Mass of the Physical Higgs Boson ($m_h$)



To isolate the mass of the observable particle (the Higgs Boson, $h$) from the full complex doublet ($\Phi$), we must choose a specific gauge[Cheng & Li, Chap. 5] where the three unphysical components (the Goldstone bosons) are absorbed by the $W^\pm$ and $Z^0$ bosons, giving them mass.

In this  gauge, the field $\Phi$ is parameterized such that only the neutral, real component takes the vacuum expectation value, and the fluctuations around it define the physical Higgs field, $\phi$:

$$\Phi(x) \approx \frac{1}{\sqrt{2}} \begin{pmatrix} 0 \\ v + \phi(x) \end{pmatrix}$$

By focusing only on this single real component $\phi$, we can simplify the potential for the mass calculation [Cheng & Li, Chap. 5] (adopting the standard convention $V(\phi) = \frac{1}{2} \mu^2 \phi^2 + \frac{1}{4} \lambda \phi^4$):

The terms 1/2 and 1/4 are added to simplify the final expression of mass.

The mass-squared is defined as [Srednicki, Chap. 2]:
$$m_h^2 = \left. \frac{\partial^2 V}{\partial \phi^2} \right|_{\phi=v}$$

1. First Derivative:
$$\frac{\partial V}{\partial \phi} = \mu^2 \phi + \lambda \phi^3$$

2. Second Derivative :
$$\frac{\partial^2 V}{\partial \phi^2} = \mu^2 + 3 \lambda \phi^2$$

3. Evaluating at the VEV ($\phi = v$):
$$m_h^2 = \mu^2 + 3 \lambda v^2$$

4. The Final Mass Relation:
We use the VEV relation derived from the first derivative (when $\frac{\partial V}{\partial \phi} = 0$): $\mu^2 = - \lambda v^2$.

Substituting this back:
$$m_h^2 = (-\lambda v^2) + 3 \lambda v^2$$

$$\mathbf{m_h^2 = 2 \lambda v^2}$$

This confirms that the Higgs Boson mass is determined by the VEV and its self-interaction coupling constant ($\lambda$). So a masse is created for the h particle !

### 4. Higgs Coupling with other Bosons

The BEH mechanism resolves the conflict where $W$ and $Z$ bosons needed to be massless for the Standard Model to be mathematically consistent (Gauge Invariant) but are experimentally observed to be massive. It links all massive fundamental particles to a single source: the **Vacuum Expectation Value (VEV)** of the Higgs Field.

#### Goldstone Boson Absorption

The core connection between the W, Z, and Higgs fields is the exchange of degrees of freedom during **Spontaneous Symmetry Breaking (SSB)**.

##### The "Eating" Mechanism
1.  The **Higgs Field** ($\Phi$) is a complex doublet, possessing four initial degrees of freedom.
2.  **SSB** occurs when the Higgs Field settles at a non-zero minimum energy value, the **VEV** ($v \neq 0$).
3.  SSB creates three **massless, unphysical** excitations called **Goldstone Bosons**.
4.  The $W^\pm$ and $Z^0$ bosons **absorb** ('eat') these three Goldstone Bosons. This provides the $W$ and $Z$ with the crucial **longitudinal polarization state** required for a Spin $J=1$ particle to be massive.

##### Consequences
* **W and Z Bosons:** Acquire their massive nature and necessary third polarization state. Their masses are generated by interaction with the VEV.
* **Higgs Boson ($h$):** The single remaining real component of the original Higgs doublet is the **physical Higgs Boson**. It is the fluctuation of the field around the VEV.

#### VEV Proportionality

The $W$ and $Z$ bosons acquire mass proportional to the VEV ($v$) and their respective Electroweak Coupling Constants ($g$ for the weak force and $g'$ for hypercharge).

| Boson | Mass Formula |
| :--- | :--- |
| **W Boson** ($W^\pm$) | $\mathbf{M_W = \frac{1}{2} g v}$ |
| **Z Boson** ($Z^0$) | $\mathbf{M_Z = \frac{1}{2} \sqrt{g^2 + g'^2} v}$ |

### 5. Higgs Coupling and Mass Proportionality

The Higgs mechanism must not only give mass to the $W$ and $Z$ bosons but also to **fermions** (quarks and leptons) without violating **Gauge Invariance**. This mass generation is handled by the **Yukawa interaction**, which directly links the coupling strength to the mass of the particle.

#### The Yukawa Interaction Term

Gauge invariance forbids explicit mass terms ($m \bar{\psi}\psi$) for fermions. Instead, their mass is generated by coupling the fermion field to the Higgs field before SSB.

The relevant term in the Lagrangian for this interaction is the **Yukawa term** ($\mathcal{L}_{\text{Yukawa}}$):

$$\mathcal{L}_{\text{Yukawa}} = -g_f \bar{\psi} \Phi \psi + \text{h.c.}$$

| Variable | Description | Nature/Role |
| :--- | :--- | :--- |
| $\mathcal{L}_{\text{Yukawa}}$ | Yukawa Lagrangian Density | Describes the interaction between the Higgs and the fermion. |
| $g_f$ | **Yukawa Coupling Constant** | A dimensionless parameter unique to each fermion $f$. |
| $\bar{\psi}, \psi$ | Fermion Fields | Field describing the matter particle and its antiparticle. |
| $\Phi$ | Complex Higgs Field Doublet | The full complex field before SSB. |
| h.c. | Hermitian Conjugate | Ensures the Lagrangian is a real number. |

#### Derivation of the Proportionality

Warning !  The potential for interaction (the Yukawa coupling gf​) exists before SSB, but the result of that interaction (the mass mf​) only emerges after the Higgs field settles into its non-zero VEV during SSB.

When Spontaneous Symmetry Breaking occurs, the Higgs field acquires its non-zero **Vacuum Expectation Value** ($v$), and we decompose the field into its VEV and the physical Higgs boson ($h$):

$$\Phi \rightarrow \frac{1}{\sqrt{2}} \begin{pmatrix} 0 \\ v + h \end{pmatrix}$$

Substituting this back into $\mathcal{L}_{\text{Yukawa}}$, the expression splits into two essential parts:

$$\mathcal{L}_{\text{Yukawa}} \rightarrow \underbrace{-\frac{g_f v}{\sqrt{2}} \bar{\psi} \psi}_{\text{Mass Term}} - \underbrace{\frac{g_f}{\sqrt{2}} \bar{\psi} h \psi}_{\text{Interaction Term}}$$

**1. The Fermion Mass Term:**
By comparing the first term to the standard mass term ($m_f \bar{\psi} \psi$), we define the mass of the fermion $f$ as:
$$m_f = \frac{g_f v}{\sqrt{2}}$$

**2. The Final Relation:**
We can now solve for the coupling constant $g_f$ and substitute it into the second term ($\mathcal{L}_{\text{coupl}}$), which describes the physical interaction between the Higgs boson ($h$) and the fermion ($\psi$):

$$g_f = \frac{\sqrt{2} m_f}{v}$$

Substituting $g_f$ into $\mathcal{L}_{\text{coupl}} = -\frac{g_f}{\sqrt{2}} \bar{\psi} h \psi$:

$$\mathcal{L}_{\text{coupl}} = - \left( \frac{\sqrt{2} m_f}{v} \right) \frac{1}{\sqrt{2}} \bar{\psi} h \psi$$

$$\mathcal{L}_{\text{coupl}} = \mathbf{- \frac{m_f}{v} \bar{\psi} h \psi}$$

Since the Vacuum Expectation Value ($v \approx 246 \text{ GeV}$) is a **universal constant**, the magnitude of the interaction (the coupling strength) is **directly proportional to the mass ($m_f$)** of the fermion.

This relationship explains why the Higgs boson interacts most frequently with the heaviest particles, such as the **Top Quark** and the $Z$ and $W$ bosons (which also gain mass proportional to $v$), justifying the experimental search strategy using heavy decay products.
## Synthesis
The mass generation for **Fermions** (quarks and charged leptons) is not caused by the VEV ($v$) alone, nor by the Yukawa coupling ($g_f$) alone, but by their essential interaction. This interaction can be understood as a clear chain of causality:

| Element | Symbol | Causal Role | Description |
| :--- | :--- | :--- | :--- |
| **Physical Cause** | $\mathbf{v}$ (VEV) | **The Source** | The non-zero, constant energy background (the vacuum). It provides the necessary potential for mass to appear. |
| **Mathematical Mechanism** | $\mathbf{g_f}$ (Yukawa Coupling) | **The Interaction Strength** | The constant that defines *how strongly* a specific fermion "couples" to the VEV. |
| **Result** | $\mathbf{m_f}$ (Fermion Mass) | **The Outcome** | The measured mass of the fermion, which is the product of the interaction strength and the vacuum background. |

The fundamental relationship is:
$$m_f = \frac{g_f v}{\sqrt{2}}$$

* If the **VEV ($v$) were zero**, all fermions would be massless, regardless of $g_f$.
* If the **Yukawa Coupling ($g_f$) were zero**, the VEV would have no effect on that specific fermion, and it would remain massless (e.g., the photon has $g_\gamma=0$).

Therefore, the **VEV** is the **physical agent** that supplies the mass, while the **Yukawa coupling** is the **governing mechanism** that dictates the amount of mass received by each fermion.

In summary, the VEV (v) is responsible for giving mass to other particles, while the Higgs boson (h) is necessary to prove that the mechanism exists and to measure its internal parameters. The Higgs boson (h) is necessary to understand how the field feels itself.


[^SF_Novaes]: S. F. Novaes (2000). "Standard Model: An Introduction" https://arxiv.org/pdf/hep-ph/0001283

[^Gauge] : Cheng, Ta-Pei, & Li, Ling-Fong., Gauge Theory of Elementary Particle Physics (1984).

[^MassPot] : Srednicki, Mark., Quantum Field Theory (2007)

[^SSB_PesKin] : Peskin, Michael E., & Schroeder, Daniel V., An Introduction to Quantum Field Theory (1995).

[^Higgs_David] : Griffiths, David J., Introduction to Elementary Particles (2008).
