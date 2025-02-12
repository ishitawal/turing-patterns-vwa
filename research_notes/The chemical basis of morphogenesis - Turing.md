## 1. A model of the embryo - morphogens

- the state of the system: description consists of the mechanical (positions, masses, velocities,...) and chemical part (chemical composition, diffusibility of each substance)
- concentrations and diffusibilities of each substance have to be given at each point
- mechanical aspects can be ignored, highlighting the chemical parts

- System consis of masses of tissues which are not growing, but contain certain substances which are reacting chemically and through which they are diffusing --> morphogens

- hormones, skin pigments --> example of morphogens

## 2. Mathematical background required


## 3. Chemical reactions

- [[The self-made tapestry_Pattern formation in nature]]
- a number of chemical substances (morphogens) diffusing through a mass of tissue of give geometrical form and reaction together within it --> reaction-diffusion system
- Laws defining patterns:
	- Laws of diffusion: each morphogen moves from regions of greater to regions of less concentration (down a concentration gradient), at a rate proportional to the gradient of the concentration, and also proportional to the "diffusibility" of the substance

	 Without cell walls: diffusibilities would be inversely proportional to the square roots of the molecular weights

	- Law of mass action: rate of which a reaction takes place is proportional to the concentrations of the reacting substances

	 Law of mass action must only be applied to the actual reactions: Ag+ + Cl- --> AgCl

- terms of the concentrations are only an approximation - would be justified if the contents were perfectly stirred --> for simplicity it is assumed


## 4. The breakdown of symmetry and homogeneity

- But a system which has spherical symmetry, and whose state is changing because of chemical reactions and diffusion, will remain spherically symmetrical for ever. --> WRONG!!!
- assumed that the deviations from spherical symmetry could be ignored - however, it is important that there are some deviations --> the system may reach a state of instability in which these irregularities or certain components of them tend to grow
- A new and stable equilibrium is usually reached with the symmetry entirely gone.

- how oscillations begin: random disturbances always present - disturbances whose frequency is the natural frequency of the oscillator will tend to set it going
- in practice, presence of irregularities (+ system has an appropriate kind of instability) --> homogeneity disappears

- p. 42 - numerical example on how small deviances grow through reaction and diffusion / guter Ansatz für Simulation

- Unstable equilibrium does not occur very naturally, usually requires some rather artificial interference
- Since systems leave unstable equilibriums --> are not often in them
- can occur naturally when a stable equil. changes into an unstable one
- p. 43, 44 --> good example for explanation of stability of a system (mouse-pendulum)


## 6. Reaction and diffusion in a ring of cells

- breakdown of homogeneity - most critical period on how to say how the system (organism) is going to develop - examination of it at any earlier time could never predict it
- no essentially new features appear when the number of morphogens is increased beyond three --> §§ 8,9 for 3 morphogens

- p. 47 - differential equations, "marginal reaction rates", "marginal reaction rate matrix"
- assumption - any further disturbances after initial one, are ignored


## 11. Restatement and biological interpretation of the results

- system in a initially stable homogeneous condition, then disturbed slightly from this state (i.e.: Brownian movement, effects of neighbouring structures or slight irregularities of form)
- disturbances might be due to changes of concentrations of a catalyst of fuel supply, ==changes of temperature==

- "linearity assumption" - system never deviated very far from the original homogeneous condition --> permitted the replacement of the general reaction rate functions by linear ones

## 13. Non-linear theory - use of digital computer

- theory depends essentially on the linearity assumption
- most of an organism is developing from one pattern in to another, rather than from homogeneity into a pattern
- with computational methods - use of non-linear equations can make more long-term predictions