


# ODE-Social-Matching-Model

Final project for the course **Introduction to Ordinary Differential Equations**  


## Project Overview

This project studies the dynamics of mutual interest between two matched users on a social networking platform using a system of ordinary differential equations (ODEs).

The goal is to understand under which conditions a relationship naturally fades out (ghosting) and when it can evolve into a stable, sustained engagement. The model captures the competition between natural interest decay and positive feedback due to mutual interaction, incorporating saturation effects inspired by logistic growth and interaction models discussed in the course.


## Mathematical Model

Let  
- $I_A(t)\$ be the interest level of user A in user B  
- $I_B(t)\$ be the interest level of user B in user A  

with $\( 0 \le I_A, I_B \le 1 \)$.

The model is given by the system:
$\dot I_A = -\alpha I_A + \beta I_B (1 - I_A),\\
\dot I_B = -\alpha I_B + \beta I_A (1 - I_B),$
where:
- $\( \alpha > 0 \)$ represents the natural decay rate of interest,
- $\( \beta > 0 \)$ represents the strength of mutual interaction.

---

## Repository Structure

```

.
├── bifurcation_diagram.py      # Transcritical bifurcation plot
├── phase_portrait.py           # Phase portrait with nullclines
├── time_series.py              # Time evolution for different scenarios
└── README.md

````


## Numerical Simulations

All simulations are implemented in Python and focus on three main aspects:

1. **Bifurcation diagram**  
   Shows a transcritical bifurcation at $\( \beta = \alpha \)$, separating ghosting and sustained engagement regimes.

2. **Phase portrait and nullclines**  
   Illustrates the geometric structure of the system and the stability of equilibrium points.

3. **Time series simulations**  
   Demonstrates how different initial interest levels evolve over time under weak and strong interaction scenarios.


## How to Run the Code

### Requirements

The simulations require Python 3 and the following packages:

- numpy
- matplotlib
- scipy

You can install the dependencies 

### Running the scripts

 **Bifurcation diagram**

```bash
python bifurcation_diagram.py
```

 **Phase portrait**

```bash
python phase_portrait.py
```

 **Time series simulations**

```bash
python time_series.py
```

Each script generates the corresponding figure used in the report.


## Results and Interpretation

The simulations confirm the analytical results derived in the report:

 When ( $\beta < \alpha$ ), the ghosting equilibrium ( (0,0) ) is stable.
 When ( $\beta > \alpha$ ), a non-trivial stable equilibrium emerges, corresponding to sustained engagement.
 Initial asymmetries in interest levels do not prevent convergence when interaction strength is sufficiently large.


## Limitations and Future Work

The model describes continuous interest dynamics and does not account for discrete events such as blocking, sudden disengagement, or external shocks. Possible extensions include stochastic perturbations or hybrid models combining continuous dynamics with discrete events.


## Author

**Chaoyang Xu**


