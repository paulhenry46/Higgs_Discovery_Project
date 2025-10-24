# Quantum Field Theory (QFT)

This document outlines the core mathematical and conceptual tools derived from Quantum Field Theory (QFT) and Special Relativity that are essential for understanding the Higgs mechanism and the experimental data analysis. The reader is not expected to read the document in one go, but to browse through it when concepts are mentioned in other documents.
## I. Quantum Field Theory (QFT) Concepts

These concepts define the theoretical framework of the Standard Model and the Higgs mechanism.

### 1. The Lagrangian Density ($\mathcal{L}$)

The Lagrangian is the central mathematical function in QFT.

* Definition: It is the difference between the kinetic energy density ($\mathcal{T}$) and the potential energy density ($\mathcal{V}$) of a system of fields:
    $$\mathcal{L} = \mathcal{T} - \mathcal{V}$$
* Role: The minimization of the Action (the integral of $\mathcal{L}$ over spacetime) determines the physical laws and equations of motion for the fields.

#### Components

The concepts of Kinetic Energy Density ($\mathcal{T}$) and Potential Energy Density ($\mathcal{V}$) are the fundamental components of the Lagrangian Density ($\mathcal{L}$) in Quantum Field Theory (QFT). They describe the energy of the field, not of a single particle.

$$\mathcal{L} = \mathcal{T} - \mathcal{V}$$

##### 1. Kinetic Energy Density ($\mathcal{T}$)

The kinetic energy density describes the energy associated with the movement or change of the field across spacetime.

For the real scalar field $\phi$, the kinetic density term involves the spacetime derivatives of the field:

$$\mathcal{T} = \frac{1}{2} (\partial^\mu \phi) (\partial_\mu \phi)$$

The term $\partial^\mu \phi$ represents the change of the field $\phi$ over position and time.

This term is non-zero only if the field is propagating (waving or vibrating). It is the energy required to create the field's motion, which, when quantized, corresponds to the Boson of Higgs ($h$)

##### 2. Potential Energy Density ($\mathcal{V}$)

The potential energy density describes the energy stored in the state of the field itself, independent of its motion.

This is the familiar Mexican Hat Potential, usually written as the negative of the non-derivative terms in the Lagrangian:

$$\mathcal{V}_{\text{Higgs}} = -\frac{1}{2} \mu^2 \phi^2 - \frac{1}{4} \lambda \phi^4$$

* Physical Role:
    * It determines the field's minimum energy state (the Vacuum Expectation Value, $v$).
    * The curvature of this potential at the minimum defines the mass of the physical particle ($m_h^2 \propto \partial^2 \mathcal{V} / \partial \phi^2$).

### 2. Gauge Invariance

The fundamental symmetry principle that makes the Standard Model consistent.

* Definition: A theory is gauge invariant if its Lagrangien ($\mathcal{L}$) remains unchanged after a local (spacetime-dependent) transformation of the fields.
* Role in Higgs Theory: This principle forbids inserting simple mass terms for the $W$ and $Z$ bosons "by hand". The Higgs mechanism is required to generate this mass while preserving the gauge invariance of the initial Lagrangian.

### 3. The Field Potential ($\mathcal{V}$) and the VEV

The potential determines the stability and energy minimum of the field.

* Definition: In the Higgs model, the potential (the "Mexican Hat") is given by:
    $$\mathcal{V}(\phi) = \frac{1}{2} \mu^2 \phi^2 + \frac{1}{4} \lambda \phi^4$$
* Role: This potential allows the field to settle into a non-zero minimum, the Vacuum Expectation Value ($v$), which triggers Spontaneous Symmetry Breaking.

### 4. Mass as the Second Derivative (Curvature)

In QFT, the mass-squared of a particle is directly linked to the curvature of its field's potential.

* Definition: The square of the Higgs Boson's mass ($m_h^2$) is the second derivative of the potential evaluated at the VEV ($\phi=v$):
    $$m_h^2 = \left. \frac{\partial^2 \mathcal{V}}{\partial \phi^2} \right|_{\phi=v}$$
* Physical Interpretation: This derivative measures the stiffness of the potential. A high curvature requires more energy (mass) to create a fluctuation ($h$) around the vacuum.

## II. Virtual Particles

The concept of a **virtual particle** (such as the $\mathbf{Z}^{*}$ in the Golden Channel $H \rightarrow Z Z^{*}$) may seem to violate fundamental laws, but it is a necessary, rigorous consequence of the **Heisenberg Uncertainty Principle** and the mathematical structure of **Quantum Field Theory (QFT)**. It does not imply the permanent creation of energy from nothing.

### 1. The Fundamental Distinction

The entire discussion hinges on the difference between a real particle, which can be measured, and a virtual particle, which acts only as a transient mediator. This difference is defined by the **mass-shell relation** from special relativity:

$$\mathbf{E^2 - (\mathbf{p}c)^2 = (mc^2)^2}$$

| Feature | **Real (On-Shell) Particle** | **Virtual (Off-Shell) Particle** |
| :--- | :--- | :--- |
| **Relativistic Constraint** | Obeys $E^2 - (\mathbf{p}c)^2 = (mc^2)^2$. | **Does not** obey the mass-shell relation. |
| **Physical Role** | Final product of a decay (e.g., the four leptons, $4\ell$). | An **internal propagator** in a Feynman diagram, mediating the force. |
| **Duration** | Can exist freely and be measured (e.g., by the tracking chambers). | Exists only for an **infinitesimal time** at an interaction vertex. |

The term "virtual" is used because the particle cannot be observed directly as a free particle; it is a mathematical necessity for describing the interaction.

### 2. The Justification: Heisenberg's Uncertainty Principle

The theoretical allowance for the off-shell state is strictly enforced by the **Energy-Time Uncertainty Principle**:

$$\mathbf{\Delta E \cdot \Delta t \gtrsim \hbar}$$

Where $\hbar$ is the reduced Planck constant. This principle introduces a fundamental uncertainty:

* **$\mathbf{\Delta E}$ (Energy Deviation):** This is the measure of how much the virtual particle deviates from its expected real mass (e.g., the amount the $\mathbf{Z}^{*}$'s mass differs from $91.2 \text{ GeV/c}^2$). It represents the local, temporary "non-conservation" of energy.
* **$\mathbf{\Delta t}$ (Lifetime):** This is the window of time during which this deviation is allowed to exist.

**The Strict Condition:** Nature permits a temporary energy fluctuation ($\mathbf{\Delta E}$) only if the duration ($\mathbf{\Delta t}$) is short enough to satisfy the relation.

* In the $H \rightarrow Z Z^{*}$ decay, the energy "debt" created by the off-shell particle must be "repaid" almost instantaneously by the decay of the $\mathbf{Z}^{*}$ into the final leptons. The overall lifetime of the $\mathbf{Z}^{*}$ is constrained by this principle.

### 3. Conservation of Energy is Maintained

The crucial point is that this local, temporary fluctuation does **not** violate the law of **global conservation of energy**:

1.  **Fixed Initial Energy:** The system starts with the precise total energy corresponding to the Higgs mass, $E_{\text{initial}} = 125 \text{ GeV}$.
2.  **Fixed Final Energy:** The total energy of all real, final products (the $4\ell$) **must exactly equal** the initial energy, $E_{\text{final}} = 125 \text{ GeV}$.

The virtual particle is the **mathematical tool** used by QFT to ensure the energy and momentum are correctly transferred from the Higgs to the four leptons, while strictly respecting the global conservation laws. No energy is permanently created or destroyed; it is merely redistributed via the $Z^{*}$ mediator under the rigorous rules of quantum mechanics.


## III. Special Relativity Concepts (Kinematics)

These tools are crucial for the experimental data analysis at the LHC.

### 1. Four-Momentum (Quadri-Vecteur Impulsion)

The relativistic combination of energy and momentum.

* Definition: The Four-Momentum $P$ of a particle is a vector with four components (using the convention $c=1$):
    $$P = (E, \vec{p}) = (E, p_x, p_y, p_z)$$
    Where $E$ is the total relativistic energy and $\vec{p}$ is the 3D momentum vector.

### 2. Invariant Mass ($M_{inv}$)

The fundamental observable used to identify new particles in collision experiments.

* Definition: It is an intrinsic property of a system of particles (Lorentz invariant), meaning its value is the same in every reference frame.
* Calculation: The squared invariant mass for a system of $N$ particles is:
    $$M_{inv}^2 = \left(\sum_{i=1}^{N} E_i\right)^2 - \left|\sum_{i=1}^{N} \vec{p}_i\right|^2$$
* Role in the Project: For the decay $H \rightarrow 4\ell$, the invariant mass calculated from the four final-state leptons ($4\ell$) is reconstructed to find the mass of the parent Higgs Boson: $M_{inv} = M_H$.