import numpy as np
import matplotlib.pyplot as plt

alpha = 1.0
beta = np.linspace(0.01, 3.0, 400)

#equilibrium branches
I0 = np.zeros_like(beta)
I_star = 1 - alpha / beta

plt.figure(figsize=(6,4))

#I* = 0 branch
plt.plot(beta[beta < alpha], I0[beta < alpha], 'k-', label=r'$I^*=0$ (stable)')
plt.plot(beta[beta > alpha], I0[beta > alpha], 'k--', label=r'$I^*=0$ (unstable)')

#non-trivial equilibrium
plt.plot(beta[beta > alpha], I_star[beta > alpha], 'b-', label=r'$I^*=1-\alpha/\beta$ (stable)')

#bifurcation point
plt.axvline(alpha, color='gray', linestyle=':', label=r'$\beta=\alpha$')

plt.xlabel(r'Interaction strength $\beta$')
plt.ylabel(r'Equilibrium interest $I^*$')
plt.title('Transcritical bifurcation diagram')
plt.legend()
plt.tight_layout()
plt.show()