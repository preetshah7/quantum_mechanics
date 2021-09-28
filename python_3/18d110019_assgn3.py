# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 17:39:23 2021

@author: preet
@rollno: 18d110019
"""
import scipy
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import sympy
from sympy.functions import exp
e = 2.7182

class Symbolic_Integral:
    ###### Define the function ########
    def func(self, x):
        return x*e**x
    
    ###### Symbolic integration #######
    def integral(self, x):
        x = sympy.symbols('x')
        val =sympy.integrate(self.func(x), x)
        return val
    
    def execute_func(self):
        x = sympy.symbols("x")
        value = self.integral(x)
        print (value)
        ######## Plotting done here ########
        x = sympy.symbols('x')
        intx=[]
        for i in np.linspace(0,3):
            intx.append(self.integral(x).evalf(subs={x: i}))
            #intx.append((i-1)*np.exp(i))
        xdata = np.linspace(0,3)
        plt.plot(xdata,self.func(xdata))
        plt.plot(xdata,intx)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend(('f(x)', 'int(f(x))' ))
        plt.savefig('int.jpg')
        plt.show()

if __name__ == "__main__":        
    integral_bin = Symbolic_Integral()
    integral_bin.execute_func()