#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Plot precomputed ΔE/V₀ vs δ² for Hydro, Ortho, and Shear strain paths.
Uses LaTeX rendering for publication-quality figures.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# USER PARAMETERS
# ==============================
use_latex = True          # Set False if no LaTeX installed
title_prefix = "MoSe2_opt"
save_format = "png"       # png or pdf

# ==============================
# MATPLOTLIB SETTINGS
# ==============================
if use_latex:
    plt.rcParams.update({
        "text.usetex": True,
        "font.family": "serif",
        "font.size": 12,
        "axes.labelsize": 11,
        "axes.titlesize": 11,
        "legend.fontsize": 11,
        "xtick.labelsize": 11,
        "ytick.labelsize": 11,
    })

# ==============================
# FUNCTION TO PLOT
# ==============================
def plot_curve():
    df = pd.read_csv("./log.lammps",skiprows=54,sep=r"\s+",nrows=1000,usecols=[0,1])
    df.columns = ["Step","PotEng"]
    delta = df["Step"].to_numpy()
    energy = df["PotEng"].to_numpy()

    plt.figure(figsize=(3.2, 3.2))
    plt.plot(delta, energy, "-", label = 'relax box')
    plt.xlabel(r"$Step~[-]$")
    plt.ylabel(r"$E_{pot}$ (eV)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"Energyminimization_MoSe2.{save_format}", dpi=600)
    plt.close()

if __name__ == "__main__":
    plot_curve()


