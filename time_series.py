import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

#ODE model
def simulate(alpha, beta, y0, T=30.0, n=800, rtol=1e-8, atol=1e-10):
    """
    Simulate the 2D ODE system on [0, T] with initial condition y0=[I_A(0), I_B(0)].

    dI_A/dt = -alpha I_A + beta I_B (1 - I_A)
    dI_B/dt = -alpha I_B + beta I_A (1 - I_B)
    """

    def f(t, y):
        Ia, Ib = y
        dIa = -alpha * Ia + beta * Ib * (1 - Ia)
        dIb = -alpha * Ib + beta * Ia * (1 - Ib)
        return [dIa, dIb]

    t_eval = np.linspace(0.0, T, n)
    sol = solve_ivp(f, (0.0, T), y0, t_eval=t_eval, rtol=rtol, atol=atol)
    return sol.t, sol.y[0], sol.y[1]

def plot_case(alpha, beta, y0_list, T, title, savepath=None):
    """
    Plot time series for multiple initial conditions under the same (alpha, beta).
    y0_list: list of tuples/lists like [(Ia0, Ib0), ...]
    """
    plt.figure(figsize=(6.5, 4.2))

    for (Ia0, Ib0) in y0_list:
        t, Ia, Ib = simulate(alpha, beta, [Ia0, Ib0], T=T)

        # plot I_A and I_B with same linestyle but different alpha transparency
        plt.plot(t, Ia, linewidth=2, label=rf'$I_A(t)$, $I_A(0)={Ia0:.2f}, I_B(0)={Ib0:.2f}$')
        plt.plot(t, Ib, linewidth=2, linestyle='--', label=rf'$I_B(t)$, $I_A(0)={Ia0:.2f}, I_B(0)={Ib0:.2f}$')

    #equilibrium levels
    if beta > alpha:
        I_star = 1.0 - alpha / beta
        plt.axhline(I_star, linestyle=':', linewidth=2, label=rf'Equilibrium $I^* = 1-\alpha/\beta = {I_star:.3f}$')
    else:
        plt.axhline(0.0, linestyle=':', linewidth=2, label=r'Equilibrium $I^* = 0$')

    plt.xlabel('Time t')
    plt.ylabel('Interest level')
    plt.ylim(-0.02, 1.02)
    plt.title(title + rf'  ($\alpha={alpha:.1f},\ \beta={beta:.1f}$)')
    plt.legend(fontsize=8, loc='best')
    plt.tight_layout()

    if savepath is not None:
        plt.savefig(savepath, dpi=200, bbox_inches='tight')

    plt.show()

#three "just right" scenarios
if __name__ == "__main__":
    alpha = 1.0
    T = 30.0

    #Case A: beta < alpha -> ghosting (interest goes to 0)
    beta_A = 0.6
    y0_list_A = [(0.6, 0.6), (0.8, 0.2)]
    plot_case(
        alpha, beta_A, y0_list_A, T,
        title='Case A: Weak interaction leads to ghosting',
        savepath=None
    )

    #Case B: beta > alpha -> sustained engagement (converges to I*)
    beta_B = 1.5
    y0_list_B = [(0.1, 0.1), (0.8, 0.2)]
    plot_case(
        alpha, beta_B, y0_list_B, T,
        title='Case B: Strong interaction leads to sustained engagement',
        savepath=None
    )

    #Case C: beta > alpha with strong asymmetry -> still converges (slow/imbalanced start)
    beta_C = 1.5
    y0_list_C = [(0.05, 0.90), (0.90, 0.05)]
    plot_case(
        alpha, beta_C, y0_list_C, T,
        title='Case C: Asymmetric initial interest still converges',
        savepath=None
    )
