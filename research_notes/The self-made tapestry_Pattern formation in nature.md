## Chapter 3 - Waves

### Off balance
- Belousov first discovered dynamical pattern formation in chemistry when researching on glycolysis - mixture of solutions changes colours in regular time intervals/ solutions mix and unmix
- does not obey 2nd law of thermodynamics - total amount of entropy/disorder must incresase
  --> preferred direction of reaction/equilibrium state
	- concept of free energy - the mechanical work that can be extracted from a system
	 free energy decreases in the direction of reaction
	 makes entropy measurable and more accessible for experimental considerations
	- coffee and milk example - can't unmix
- still reaches a stable equilibrium after oscillations - but why the detour to reach it?
- 2nd law of therm. only applies to equilibrium states
	- non-equilibrium rhythms of life (carbon cycle,...) actively maintain a certain state
	- such systems need a supply of energy or will otherwise decay into equilibrium
	- energy --> pattern
- Energy supply
	- environment - sun
	- CSTRs (continuous stirred-tank reactors) - steady flow of reactants and withdrawal of end-products (e.g. reactions or human bodies)

### The chemical seesaw 

==Topic: autocatalysis = non-linearity==

- key point in BZ reaction (and activator-inhibitor systems): self-catalysis/autocatalysis
	- catalysts speed up the reaction rate of a reaction without being changed by the process
	 however when splitting the entire process into sub-reactions we can see that catalysts react with the other reactants forming different molecular structures, and after completion are restored again
	 *video: give a simple example for such a reaction* (A+B -->C....)
	- autocatalysis is a special case of catalysis where one of the products functions as a catalyst and produces more product molecules creating a positive feedback process
	 on its own it would simply create products at an exponential rate making the reaction faster and faster and getting out of control
	- reason why this process does not explode is that positive feedback processes tend to use up more reactants than can be supplied, even in a CSTR --> concentration of reactants falls = autocatalytic process dies, competing reaction can take over --> different coloured products, uses up all reactants and dies down --> oscillating
- limit cycles p. 54
- oscillations are patterns in time
### Going places
- in a CSTR the concentration a reactant is the same in the entire system, in an unstirred tank however small differences in concentration will occur, because of the postivie-feedback behaviour of the system minor changes can blow out of proportion resulting in different concentrations, colour,... from region to region --> pattern formation
	- "patterns generic to a whole class of non-equilibrium systems in chemistry"
	- patterns can be captured by by letting the reaction run in a gel medium --> slow down the rate of diffusion and stabilising the pattern
- non-uniform mixture - excitable medium: "such a medium can change its state locally when some stimulus (eg concentrations of chemical species) reaches a certain threshold"
  but importantly the medium has to go through a refractory period, in which it can not be excited again, to form these complex patterns
- cellular automaton model - computational model from the 1950s for modelling self-arranging spatio-temporal patterns using the idea of an excitable medium (p.57)
### Burn up
- cellular flames - experiment?
	p. 64/65

### Going wild (p.67)
- chaos in the BZ reaction through increased flow rate or initial concentrations of the reagents
	- period-doubling bifurcation
- Hopf bifurcation = abrupt transition from a stable, steady state to an oscillatory one
	- a common source of periodic motion from initially steady motion

## Chapter 4 -  Bodies

- Question of morphogenesis / symmetry breaking: How can a almost spherically symmetrical ball of cells break its symmetry and develop differently to form organs and limbs?

>Turing - Chemical basis of morphogenesis: describes a hypothetical chemical reaction that could generate spontaneous symmetry breaking, leading to stable spatial patterns, in an initially uniform mixture of chemical compounds. This hypothetical reaction was supposed to function as a model for pattern formation in an embryo.(The self-made tapestry, pattern formation in nature, Philip Ball, p.79)[[The chemical basis of morphogenesis - Turing]]

- Remarkable: proposed that diffusion of a chemical (morphogen) causes and drives this symmetry breaking --> naturally goes against intuition (*video: example with water and paint*)
- Diffusion is competing with a autocatalytic chemical reaction = reaction-diffusion system
	- autocatalytic = non-linear
	- excitable reaction-diffusion systems = travelling waves (BZ-reaction)
	- excitable reaction-diffusion systems + under certain conditions = stationary patterns
- excitable reaction-diffusion systems (BZ reaction - chapter waves (Ball P.))

![[10-Figure2.3-1.png]]

- Activator-inhibitor system (subset of reaction-diff. system):
    - Key element for spatial patterns: A and B diffuse at different rates (inhibitor diffuses faster) —> different effective rages of their respective influences —> can dominate in distinct regions
    - Long-range inhibition / localized short-range activation
- Turing made equations linear (lack of technology) —> unstable against perturbations
- later non-linear equations (Meinhardt and Gierer)

- tempted to think that in a equilibrium state however pattern is dynamic (constant reaction)
- homogenous medium in a symmetry-breaking instability + increased driving force away from equilibrium = pattern

Key questions:
- What causes the symmetry breaking in the case of Turing Patterns or the experiment?
		p. 79 - diffusion is the driving force for symmetry breaking
		small disturbances which are increased through diffusion - Turing - Chemical basis of morphogenisis

### Turing mechanism (stationary pattern)vs BZ reaction (travelling waves)

- Turing and Belousev discovered their findings around the same time
- both results of reaction-diffusion systems and Arthur Winfree proved that the BZ reaction resulted from "an activator-inhibitor pattern-formation process in the poorly mixed BZ mixture"
- both the result of non-linearities, autocatalysis and feedbacks in chemical reactions that produce them
- however mechanism behind instability are different
- So what's the important difference between them?
	- Turing patterns: "only if the response of the inhibitor to changes in activator concentration is rapid (which in turn means that the processes that remove the inhibitor must be fast relative to those that remove the activator)"
	- BZ-like oscillations: inhibitor is present for a long time or no difference between the rates of diffusion of the different chemical species --> difference essential for Turing patterns
	- BZ: inhibitor diffuses less rapidly than activator; local disturbance instead of global symmetry breaking

- The Brusselator = theoretical model

### CIMA-reaction (p.82 ff.)

- chlorite and iodide ions and malonic acid in a thin layer of gel that was continuously fed from opposite direction with fresh reagents
- activator = iodide
  inhibitor = chlorite
- starch is colour-changing indicator changing from yellwo ot blue when binding with tir-iodide ions
- difference of diffusion rates possible with polymer (starch) gel where iodide is reacting with iodide
- was tricky to achieve a difference in diffusion rates

### Environmental factors and reaction conditions _ CIMA_
- Qi Ouyang and Harry Swinney found out that pattern disappeared if gel was warmed above 18°C and reappeared when cooled down again
- able to achieve different patterns by changing conditions / concentrations: more iodide / lower malonic acid broke symmetry differently --> stripes instead of dots
- Turing patterns dependent on dimensions, size and shape of the container
	- minimum size: characteristic size determined by diffusion rate (diameter of a dot=no pattern, needs to be larger than that)