# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 12:08:33 2021

@author: preet
@rollno: 18d110019
"""
import matplotlib.pyplot as plt
import numpy as np

class Function:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def comp_func(self, x, a, b):
        return a*np.exp(x) + b*np.exp(-x)
    
    def execute_fitting(self):
        xdata = np.linspace(-6, 6, 300)
        ydata = self.comp_func(xdata, self.a, self.b)
        # Plot the actual data
        plt.scatter(xdata, ydata, s=5)
        # The actual curve fitting happens here
        p2 = np.polyfit(xdata,ydata,2)
        print(p2, np.poly1d(p2))
        p3 = np.polyfit(xdata,ydata,3)
        p4 = np.polyfit(xdata,ydata,4)
        plt.plot(xdata, np.polyval(p2,xdata), 'r-')
        plt.plot(xdata, np.polyval(p3,xdata), 'b-')
        plt.plot(xdata, np.polyval(p4,xdata), 'g-')
        # Show the graph
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend(( 'p_2', 'p_3', 'p_4', 'data'))
        plt.savefig("18d110019_polyfit2.png")
        plt.show()
 
#(i)
#func_bin = Function(2,3)
#func_bin.execute_fitting()

#(ii)
func_bin = Function(4,6)
func_bin.execute_fitting()