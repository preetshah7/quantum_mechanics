#!/bin/usr/python from sys import extt from sys import argv
"""
@author: preet
@roll: 18d110019
"""
import numpy as np
from sys import exit
from sys import argv
import os
import shutil

band_index= 72
E_fermi= 10.1597 # run $(grep E-fermi OUTCAR) on the given OUTCAR

nband=range(band_index)
def analyse_out(filename= "EIGENVAL"):
    f1= open( "data_up.dat", "w")
    f2= open( "data_down.dat", "w")
    for i in range(len(nband)):
        data_file= open(filename, "r")
        for line in data_file:
            if (line.find(' '+ str(nband[i]+1) + ' ')>=0):
                energy_stat_up= float(line.split()[1])- (E_fermi)
                energy_stat_down= float(line.split() [2])-(E_fermi)
                print(energy_stat_up)
                print(energy_stat_down)
                f1.write("%20.10f" % energy_stat_up)
                f2.write("%20.10f" % energy_stat_down)
        f1.write("\n")
        f2.write("\n")
    f1.close()
    f2.close()

energy_stat=analyse_out(filename='EIGENVAL' )

up_data= open("data_up.dat", 'r')
mat_up =[]
for line in up_data:
    mat_up.append(list(map(float, line.split()[:])))
mat_up_t=np.transpose(mat_up)
print(mat_up_t)
np.savetxt('band_up.txt', mat_up_t)
up_data.close()

down_data= open("data_down.dat", 'r')
mat_down =[]
for line in down_data:
    mat_down.append(list(map(float, line.split()[:])))
mat_down_t=np.transpose(mat_down)
print(mat_down_t)
np.savetxt('band_down.txt', mat_down_t)
down_data.close()