#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 12:40:57 2024

@author: ygn
"""

import pandas as pd
import numpy as np

num_atoms = 810

nframes = 1

for i in range(nframes):
    df = pd.read_csv(r"./dump.emin.lammpstrj",skiprows=9+i*(num_atoms+9),header=None,nrows=num_atoms,sep=r"\s+",usecols=[1,2,3,4])
    df.columns = ["atype","x","y","z"]
    type_arr = []
    for _ in df["atype"].tolist():
        if _ == 1:
            type_arr.append("Mo")
            
        elif _ == 2:
            type_arr.append("Se")
            
    df["atype"] = type_arr
    f = open("./dump.xyz", "a")
    f.write(f"{num_atoms}\n")
    f.write("\n")
    f.close()
    df.to_csv(r"./dump.xyz",header=None,index=None,sep=" ",mode="a")
