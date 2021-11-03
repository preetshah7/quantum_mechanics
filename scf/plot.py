# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 00:22:13 2021

@author: preet
"""
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
from matplotlib.pyplot import figure

figure(figsize=(10, 6), dpi=80)
df = pd.read_csv('kpoint.dat', sep=' ', header=None)
df = df.sort_values(by=[0], ascending=True)
plt.plot(df[0], df[1], color='tab:purple', marker='o')
plt.title('18d110019 : Energy difference vs k-points', fontsize=14)
plt.xlabel('k points (kxkxk)', fontsize=14)
plt.ylabel('E-diff', fontsize=14)
plt.grid(True)
plt.savefig('kpoint.png')
plt.show()

figure(figsize=(10, 6), dpi=80)
df = pd.read_csv('strain.dat', sep=' ', header=None)
df = df.sort_values(by=[0], ascending=True)
plt.plot(df[0], df[1], color='tab:orange', marker='o')
plt.title('18d110019 : Lattice strain vs Total enegy', fontsize=14)
plt.xlabel('lattice strain (l-l_0)/l_0', fontsize=14)
plt.ylabel('E_tot(eV)', fontsize=14)
plt.grid(True)
plt.savefig('strain.png')
plt.show()

figure(figsize=(10, 6), dpi=80)
df = pd.read_csv('cutoff.dat', sep=' ', header=None)
df = df.sort_values(by=[0], ascending=True)
plt.plot(df[0], df[1], color='tab:red', marker='o')
plt.title('18d110019 : Plane wave energy cutoff vs Total enegy', fontsize=14)
plt.xlabel('cutoff Energy', fontsize=14)
plt.ylabel('E_tot(eV)', fontsize=14)
plt.grid(True)
plt.savefig('cutoff.png')
plt.show()