#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.size": 12,
    "axes.labelsize": 12,
    "axes.titlesize": 12,
    "legend.fontsize": 10,
    "xtick.labelsize": 11,
    "ytick.labelsize": 11
})

data = np.loadtxt("stress_avg.txt", comments="#")

timestep = data[:, 0]
pxx = data[:, 1]
pyy = data[:, 2]
pxy = data[:, 3]

epsilon = timestep*1e-7
Syy = pyy*-1e-4
# ---- Plot ----
fig, ax = plt.subplots(figsize=(3.6, 3.6))
ax.plot(epsilon, Syy, lw=2, color="red")

ax.set_xlabel(r"strain $\epsilon$")
ax.set_ylabel(r"stress $\sigma_{yy}$ (GPa)")
ax.set_title(r"(b) $\dot{\epsilon_y} == 10^{-4}/ps$", pad=10)
ax.set_xlim([0,0.25])

fig.tight_layout()
fig.savefig("sigmayy.png", dpi=600)
plt.show()
