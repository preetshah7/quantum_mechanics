# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 15:36:13 2021

@author: preet
@rollno: 18d110019
"""
# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

class Graphene:

    def __init__(self, a, E2p):
        self.a = a
        self.E2p = E2p
        self.r1 = -3.033 #eV
        self.r0 = 0.129 #eV

    def make_data(self):
        # Make data.
        kX = np.arange(-2, 2, 0.1)
        kY = np.arange(-2, 2, 0.1)
        kX, kY = np.meshgrid(kX, kY)
        gK = np.sqrt(1 + 4*np.cos(3**0.5/2*kY*self.a)\
         *np.cos(kX*self.a/2) + 4*np.cos(kX*self.a/2)**2)
        EjK1 = (self.E2p + self.r1*gK)/(1 + self.r0*gK)
        EjK2 = (self.E2p - self.r1*gK)/(1 - self.r0*gK)

        return kX, kY, EjK1, EjK2

    def tb_plot(self):
        
        kX, kY, EjK1, EjK2 = self.make_data()
        
        # Creating figure
        fig = plt.figure(figsize =(14, 9))
        ax = fig.add_subplot(111, projection='3d')
          
        # Creating plot
        ax.plot_surface(kX, kY, EjK1, rstride=1, cstride=1,\
        cmap=cm.viridis, vmin=-10, vmax=15)   #surface 1
        ax.plot_surface(kX, kY, EjK2, rstride=1, cstride=1,\
        cmap=cm.viridis, vmin=-10, vmax=15)  #surface 2
        
        ax.set_xlabel('Kx (A^-1)')
        ax.set_ylabel('Ky (A^-1)')
        ax.set_zlabel('Energy (eV)') 
        ax.set_title('Graphene Tight Binding model')
        ax.view_init(elev=7, azim=-69)
        ax.text(0.8, 0, 11, "E+", color='black', fontsize='large')
        ax.text(0, 0, -8, "E-", color='black', fontsize='large')
        ax.set_zlim(-10,15) 
        
        plt.xticks(np.arange(-2, 2, step=1))  # Set label locations.
        plt.yticks(np.arange(-2, 2, step=1))
        plt.savefig('Graphene Tight Binding model.eps')
        plt.savefig('Graphene Tight Binding model.png')
        # show plot
        plt.show()

    def twodim_plot(self):
        
        kX = np.arange(-3, 3, 0.1)
        gK = np.sqrt(1 + 4*np.cos(kX*self.a/2)\
         + 4*np.cos(kX*self.a/2)**2)
        EjK1 = (self.E2p + self.r1*gK)/(1 + self.r0*gK)
        EjK2 = (self.E2p - self.r1*gK)/(1 - self.r0*gK)
        
        # Creating figure
        fig = plt.figure(figsize =(14, 9))
        ax = fig.add_subplot(111)
        ax.plot(kX, EjK1, color='tab:blue')
        ax.plot(kX, EjK2, color='tab:orange')
        
        ax.axhline(y=0, color='black')
        ax.axvline(x=0, color='black')
        
        ax.set_xlabel('Kx')
        ax.set_ylabel('Ej(k) (eV)')
        ax.text(1.7, -2, "K+", color='black', fontsize='xx-large')
        ax.text(-1.7, -2, "K-", color='black', fontsize='xx-large')
        ax.set_title('Graphene 2D-energy plot')
        plt.savefig('Graphene 2D-energy plot.eps')
        plt.savefig('Graphene 2D-energy plot.png')
        # show plot
        plt.show()

if __name__=='__main__':
    # a = 2.46 Ao
    orb_bin = Graphene(2.46, 0)
    orb_bin.tb_plot()
    orb_bin.twodim_plot()