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
title_prefix = "MoSe2_npt"
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
    df = pd.read_csv("./log.lammps",skiprows=54,sep=r"\s+",nrows=5000,usecols=[0,1,2,3,4,5,6])
    df.columns = ["Step","PotEng","KinEng","TotEng","Temp","Lx",'Ly']
    time = df["Step"].to_numpy()*0.001
    pe = df["PotEng"].to_numpy()
    ke = df["KinEng"].to_numpy()
    etot = df["TotEng"].to_numpy()
    temp = df["Temp"].to_numpy()
    Lx = df["Lx"].to_numpy()
    Ly = df["Ly"].to_numpy()


    plt.figure(figsize=(3.2, 3.2))
    plt.plot(time, Lx, color = "r", label = '$L_x$')
    plt.plot(time, Ly, color = "b", label = '$L_y$')
    plt.xlabel(r"$Time~[ps]$")
    plt.ylabel(r"$L_x~[\AA]$")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"EnergyL_MoSe2.{save_format}", dpi=600)
    plt.close()

if __name__ == "__main__":
    plot_curve()


