# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 12:45:44 2021

@author: preet
@rollno: 18d110019
"""
import matplotlib.pyplot as plt
import numpy as np
import sympy

class LJmodel:
    
    def __init__(self):
        """
        A = 1.024 × 10−23 (Jnm^6)
        B = 1.582 × 10−26 (Jnm^12)
        Hints: It is easier if you divide A and B by the Boltzmann’s constant,
        1.381 × 10−23JK−1 so as to measure V(r) in units of K
        A = 0.7417 (Knm^6)
        B = 1.1455 x 10-3 (Knm^12)
        """
        self.A = 0.7417
        self.B = 1.1455 * 10**-3
        
    def compute_func(self, r, A, B):
        
        r = sympy.symbols('r')
        Vr = (B/r**12) - (A/r**6)
        Fr = -sympy.diff(Vr, r)
        return Vr, Fr
    
    def execute_plotting(self):
        
        r = sympy.symbols('r')
        Vr, Fr = self.compute_func(r, self.A, self.B)
        
        print(Vr, Fr)
        
        V=[]
        F=[]
        eq_separation = []
        for i in np.linspace(0.3,0.8):
            V.append(Vr.evalf(subs={r: i}))
            F.append(Fr.evalf(subs={r: i}))
            if abs(Fr.evalf(subs={r: i}))<1 :
                eq_separation.append(i)
            else:
                continue
        print(F)
        print(f"The euilibrium separation is {eq_separation[0]}nm.")
        
        x = np.linspace(0.3,0.8)
        plt.plot(x,V)
        plt.xlabel("r - distance from nucleus")
        plt.ylabel("V (in K)")
        plt.legend('V(r)')
        plt.savefig('LJ_model_V.png')
        plt.show()
        
        x = np.linspace(0.3,0.8)
        plt.plot(x,F)
        plt.xlabel("r - distance from nucleus")
        plt.ylabel("F (in Knm-1)")
        plt.legend('F(r)')
        plt.savefig('LJ_model_F.png')
        plt.show()
        
LJmodel_bin = LJmodel()
LJmodel_bin.execute_plotting()
# Output recieved - The euilibrium separation is 0.38163265306122446nm.