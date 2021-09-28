# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 20:43:11 2021

@author: preet
@rollno: 18d110019
"""
import numpy as np
from matplotlib.pylab import plt
import math

class projectile:
    """
    We build a common class for getting the projectile motion for with & without
    drag force.
    angle-> angle of release
    v0-> inintial velocity
    time-> time of observations(may differ from time of flight)
    """
    def __init__(self, angle, v0, time, drag_coeff = 0):
        # set drag_coeff as an optional argument
        self.angle = angle
        self.v0 = v0
        self.time = time
        self.drag_coeff = drag_coeff
        
    def without_drag(self, angle, v0, time):
        t = np.linspace(0,time,300)
        dt = t[1] - t[0] #s
        g = 9.8 # m/s2
        m = 1 # kg
        # Distribute initial velocity to x and y.
        v0 = v0 # m/s
        vx = v0*np.cos(angle)
        vy = v0*np.sin(angle)
        y0 = 0
        x0 = 0
        vg = 0
        y_list = [y0]
        x_list = [x0]
        ax=0
        ay= -g
        for i in range(1, len(t)):
        # Update y.
            vg += ay * dt
            y0 += (vg + vy)* dt
            # Update x.
            x0 += vx * dt
            # Stop updating when it hits ground at y=0.
            if y0 > 0:
                y_list.append(y0)
                x_list.append(x0)
            else:
                break
        # (max x, max t)
        return x_list, y_list
    
    def with_drag(self, angle, v0, time, drag_coeff):
        t = np.linspace(0,time,300)
        dt = t[1] - t[0] #s
        g = 9.8 # m/s2
        m = 1 # kg
        # Distribute initial velocity to x and y.
        v = v0 # m/s
        theta = angle #radians
        y0 = 0
        x0 = 0
        y_list = [y0]
        x_list = [x0]
        for i in range(1, len(t)):
            # Distribute initial velocity to x and y.
            drag_force = drag_coeff * v**2
            vx = v*np.cos(theta)
            vy = v*np.sin(theta)
            ax = -drag_force * np.cos(theta)
            ay = -g -drag_force * np.sin(theta)
            # Update y.
            vy += ay * dt
            y0 += vy * dt
            # Update x.
            vx += ax * dt
            x0 += vx * dt
            
            v = math.sqrt(vx**2 + vy**2)
            theta = math.atan(vy/ vx)
            print(theta)
            # Stop updating when it hits ground at y=0.
            if y0 > 0:
                y_list.append(y0)
                x_list.append(x0)
            else:
                break
        # (max x, max t)
        return x_list, y_list
    
    def plot_motion(self):
        
        if (self.drag_coeff == 0):
            x_list1, y_list1 = self.without_drag(self.angle,\
                                               self.v0, self.time)
            print("Projectile motion without drag")
        else:
            x_list1, y_list1 = self.with_drag(self.angle,\
                                              self.v0, self.time, self.drag_coeff)
            print("Projectile motion with drag")
            
        print (x_list1, y_list1)
        plt.plot(x_list1, y_list1)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.savefig('projectile1_18d110019')
        plt.show()

"""
(i)
output_motion = projectile(np.pi/4, 60, 25)
output_motion.plot_motion()
"""
#(iib)
output_motion = projectile(np.pi/3, 30, 30, 0.05)
output_motion.plot_motion()
"""
(iia)
For range we simply run for time period to get last value of x
output_motion = projectile(np.pi/3, 30, 100, 0.05)
output_motion.plot_motion()
Range-> 55.818321098538036 m
"""