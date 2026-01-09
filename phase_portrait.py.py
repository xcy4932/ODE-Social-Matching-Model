import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

#Parameters
alpha = 1.0
beta = 1.5
T = 20.0

#ODE model
def vector_field(Ia, Ib):
    dIa = -alpha * Ia + beta * Ib * (1 - Ia)
    dIb = -alpha * Ib + beta * Ia * (1 - Ib)
    return dIa, dIb

def system(t, y):
    Ia, Ib = y
    dIa, dIb = vector_field(Ia, Ib)
    return [dIa, dIb]

#vector field
grid_n = 25
Ia_grid = np.linspace(0.0, 1.0, grid_n)
Ib_grid = np.linspace(0.0, 1.0, grid_n)
IA, IB = np.meshgrid(Ia_grid, Ib_grid)
dIA, dIB = vector_field(IA, IB)

plt.figure(figsize=(6, 6))
plt.streamplot(IA, IB, dIA, dIB, color='gray', density=1.1, linewidth=1.2, arrowsize=1.2)

#Plot: nullclines
#dIa = 0  =>  Ib = (alpha * Ia) / (beta * (1 - Ia))
#dIb = 0  =>  Ia = (alpha * Ib) / (beta * (1 - Ib))
eps = 1e-4  # avoid division by zero near 1
Ia_nc = np.linspace(0.0, 1.0 - eps, 600)
Ib_from_dIa0 = (alpha * Ia_nc) / (beta * (1.0 - Ia_nc))

#Keep only the portion inside [0,1]
mask1 = (Ib_from_dIa0 >= 0.0) & (Ib_from_dIa0 <= 1.0)
plt.plot(Ia_nc[mask1], Ib_from_dIa0[mask1], linestyle='--', linewidth=2,
         label=r'Nullcline $\dot I_A=0$')

Ib_nc = np.linspace(0.0, 1.0 - eps, 600)
Ia_from_dIb0 = (alpha * Ib_nc) / (beta * (1.0 - Ib_nc))

mask2 = (Ia_from_dIb0 >= 0.0) & (Ia_from_dIb0 <= 1.0)
plt.plot(Ia_from_dIb0[mask2], Ib_nc[mask2], linestyle='--', linewidth=2,
         label=r'Nullcline $\dot I_B=0$')

#trajectories
initial_conditions = [
    [0.10, 0.10],
    [0.80, 0.20],
    [0.20, 0.80],
    [0.60, 0.60],
    [0.05, 0.90],
]

t_eval = np.linspace(0.0, T, 600)
for y0 in initial_conditions:
    sol = solve_ivp(system, (0.0, T), y0, t_eval=t_eval, rtol=1e-8, atol=1e-10)
    plt.plot(sol.y[0], sol.y[1], linewidth=2)

#equilibria
#Ghosting equilibrium
plt.plot(0.0, 0.0, 'ro', markersize=9, label='Ghosting equilibrium')

#Stable non-trivial equilibrium when beta > alpha
if beta > alpha:
    I_star = 1.0 - alpha / beta
    plt.plot(I_star, I_star, 'bo', markersize=9, label='Stable equilibrium')

#Final cosmetics
plt.xlabel(r'$I_A$')
plt.ylabel(r'$I_B$')
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.title(rf'Phase portrait ($\alpha={alpha:.1f},\ \beta={beta:.1f}$)')

plt.legend(loc='lower right', frameon=True)

plt.tight_layout()

plt.show()
