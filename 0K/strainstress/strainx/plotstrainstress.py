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
Sxx = pxx*-1e-4
# ---- Plot ----
fig, ax = plt.subplots(figsize=(3.6, 3.6))
ax.plot(epsilon, Sxx, lw=2, color="blue")

ax.set_xlabel(r"strain $\epsilon$")
ax.set_ylabel(r"stress $\sigma_{xx}$ (GPa)")
ax.set_title(r"(a) $\dot{\epsilon_x} == 10^{-4}/ps$ at 0 K", pad=10)
ax.set_xlim([0,0.4])

fig.tight_layout()
fig.savefig("sigmaxx.png", dpi=600)
plt.show()
