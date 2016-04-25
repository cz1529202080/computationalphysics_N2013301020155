# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 11:01:46 2016
@author: AF
"""

#import ode as solving_ode
import matplotlib.pyplot as plt
import numpy as np
from visual import *

def correct(string):
    for i in range(len(string)):
        if ( string[i] > 3.1415 ):
            for j in range(i,len(string)):
                string[j] = string[j] - 2*np.pi 
        elif ( string[i] < -3.1415 ):
            for k in range(i,len(string)):
                string[k] = string[k] + 2*np.pi
        else:
            pass
    return string

def correct_single(string):
    while string > np.pi:
        string = string - 2*np.pi 
    while string < - np.pi:
        string = string + 2*np.pi
    return string

def select(string,period):
    record = [[],[[],[]]]
    for i in range(len(string[0])):
        if (abs(string[0][i]%(period)) <0.0001):
            record[0].append(string[0][i])
            record[1][0].append(correct_single(string[1][0][i]))
            record[1][1].append(string[1][1][i])
        else:
            pass
    return record

class harmonic:
    def __init__(self,dt,a,b,x_0):
        self.dt= dt
        self.a = a
        self.x_0 = x_0
        self.N = int((b - self.a)/(self.dt))
                
    def calculate(self):
        self.w = []
        self.x = []
        self.t = []
        self.t.append(self.a)
        self.w.append(0)
        self.x.append(self.x_0)
        for i in range(1,self.N):
            self.w.append(self.w[i - 1] - np.sin(self.x[i - 1])*self.dt - 0.5*self.w[i - 1]*self.dt + 1.2*np.sin(2./3*self.t[i - 1])*self.dt)
            self.x.append(correct_single(self.x[i - 1] + self.w[i] * self.dt))
            self.t.append(self.t[i - 1] + self.dt)
        return self.t, self.x, self.w
        
    def calculate_s(self):
        self.w = []
        self.x = []
        self.t = []
        self.t.append(self.a)
        self.w.append(0)
        self.x.append(self.x_0)
        for i in range(1,self.N):
            self.w.append(self.w[i - 1] - np.sin(self.x[i - 1])*self.dt - 0.5*self.w[i - 1]*self.dt + 1.2*np.sin(2./3*self.t[i - 1])*self.dt)
            self.x.append(self.x[i - 1] + self.w[i] * self.dt)
            self.t.append(self.t[i - 1] + self.dt)
        return self.t, self.x, self.w

    def vplot(self):
        roof = box (pos=(0,10,0), length=4, height=0.3, width=4, material = materials.wood)
        pendulum = sphere(pos=(10*np.sin(self.x_0),10-10*np.cos(self.x_0),0),radius = 1, material = materials.wood)
        pendulum.theta = 0.2
        pendulum.omega = 0
        rope = curve(pos = [roof.pos, pendulum.pos])
        force_D = arrow(pos = pendulum.pos, axis = (6*np.cos(self.x_0),6*np.sin(self.x_0),0), color = color.yellow, shaftwidth=0.5)
        deltat = 0.04
        t = 0
        i = 0
        while i < len(self.w):
            rate(100)
            pendulum.omega = self.w[i]
            pendulum.theta = pendulum.theta + pendulum.omega*deltat
            pendulum.pos = (10*np.sin(pendulum.theta),10-10*np.cos(pendulum.theta),0)
            F = 6*np.sin(2./3*t)
            force_D.pos = pendulum.pos
            force_D.axis = (F*np.cos(pendulum.theta),F*np.sin(pendulum.theta),0)
            rope.pos = [roof.pos, pendulum.pos]
            t = t + deltat
            i+=1
        
        
        
plt.figure(figsize = (18,12))
### --------------- Second-order Runge-Kutta ----------
'''A = solving_ode.ode((2*np.pi/(1.95/3))/100,0,20000,(0.2,0))  
A.set_fx(('w','-np.sin(x)-0.5*w+1.20*np.sin(1.95/3*t)'),['t','x','w'])
rgkt_2_record = A.rgkt_2()[:]
rgkt_3_record = select(rgkt_2_record,(2*np.pi/(1.95/3)))'''
'''B = solving_ode.ode((2*np.pi/(2.00/3))/100,0,20000,(0.2,0))  
B.set_fx(('w','-np.sin(x)-0.5*w+1.20*np.sin(2.00/3*t)'),['t','x','w'])
rgkt_4_record = B.rgkt_2()[:]
rgkt_5_record = select(rgkt_4_record,(2*np.pi/(2.00/3)))
C = solving_ode.ode((2*np.pi/(2.05/3))/100,0,20000,(0.2,0))  
C.set_fx(('w','-np.sin(x)-0.5*w+1.20*np.sin(2.05/3*t)'),['t','x','w'])
rgkt_6_record = C.rgkt_2()[:]
rgkt_7_record = select(rgkt_6_record,(2*np.pi/(2.05/3)))'''
### -----------------------------------------------
'''plt.figure(figsize = (12,6))
B = harmonic(3*np.pi/1000,0,100,0.2)
euler_c_record_1 = B.calculate()[:]
euler_c_record_2 = B.calculate_s()[:]
plt.subplot(121)
plt.xlabel('Time (s)')
plt.ylabel('Theta (radians)')
plt.plot(euler_c_record_1[0], euler_c_record_1[1])
plt.subplot(122)
plt.xlabel('Time (s)')
plt.ylabel('Theta (radians)')
plt.plot(euler_c_record_2[0], euler_c_record_2[1])'''
### ------------------ plot  --------------------------
#plt.figure(figsize = (12,6))
#plt.subplot(121)
#plt.scatter(correct(rgkt_3_record[1][0]),rgkt_3_record[1][1],s=1,label = '2th-order Runge-Kutta method')
'''plt.xlabel(r'$\theta$ (radians)')
plt.ylabel(r'$\omega$ (radians/s)')
plt.scatter(correct(rgkt_4_record[1][0]),rgkt_4_record[1][1],s=1,label = r'$F_D =1.2$, $\Omega = 2/3$')
plt.legend(loc = 'upper left')'''
#plt.subplot(122)
'''plt.xlabel('Theta(radians)')
plt.ylabel('Angular velocity (radians/s)')
plt.scatter(rgkt_3_record[1][0],rgkt_3_record[1][1],s=10,label = r'$\Omega_D=$'+' 1.95/3')
plt.scatter(rgkt_5_record[1][0],rgkt_5_record[1][1],s=10,c ='r',label = r'$\Omega_D=$'+' 2.00/3')
plt.scatter(rgkt_7_record[1][0],rgkt_7_record[1][1],s=10,c ='g',label = r'$\Omega_D=$'+' 2.05/3')
plt.legend(loc = 'upper left')'''
##  --------------- delta theta -----------------------
'''A = solving_ode.ode(0.04,0,200,(0.2,0))  
A.set_fx(('w','-np.sin(x)-0.5*w+1.2*np.sin(2./3*t)'),['t','x','w'])
rgkt_2_record = A.rgkt_2()[:]
B = solving_ode.ode(0.04,0,200,(0.2,0))
B.set_fx(('w','-np.sin(x)-0.5*w+1.2*np.sin((2.01/3)*t)'),['t','x','w'])
rgkt_3_record = B.rgkt_2()[:]
delta_theta_record_2 = []
for i in range(len(rgkt_2_record[0])):
    delta_theta_record_2.append(rgkt_2_record[1][1][i] - rgkt_3_record[1][1][i])
plt.subplot(132)
plt.semilogy(rgkt_2_record[0],delta_theta_record_2,lw=2)
plt.ylim(0,10)
plt.xlabel('Time (s)')
plt.ylabel(r'$\Delta\theta$'+'(radians)')'''
## ----------------- delta force ---------------------
'''A = solving_ode.ode(3*np.pi/100,0,100000,(0.2,0))  
A.set_fx(('w','-np.sin(x)-0.5*w+1.2*np.sin(2./3*t)'),['t','x','w'])
rgkt_3_record = select(A.rgkt_2())[:]
plt.subplot(131)
plt.xlabel('Theta(radians)')
plt.ylabel('Angular velocity (radians/s)')
plt.scatter(rgkt_3_record[1][0],rgkt_3_record[1][1],s=1,label = r'$F_D$'+'=1.2')
plt.legend(loc = 'upper right')
A = solving_ode.ode(3*np.pi/100,0,100000,(0.2,0))  
A.set_fx(('w','-np.sin(x)-0.5*w+1.3*np.sin(2./3*t)'),['t','x','w'])
rgkt_3_record = select(A.rgkt_2())[:]
plt.subplot(133)
plt.xlabel('Theta(radians)')
plt.ylabel('Angular velocity (radians/s)')
plt.scatter(rgkt_3_record[1][0],rgkt_3_record[1][1],s=1,label = r'$F_D$'+'=1.3')
plt.legend(loc = 'upper right')'''
'''plt.subplot(231)
A = solving_ode.ode(3*np.pi/100,0,20000,(0.2,0))  
A.set_fx(('w','-np.sin(x)-0.5*w+1.15*np.sin(2./3*t)'),['t','x','w'])
rgkt_2_record = A.rgkt_2()[:]
rgkt_3_record = select(rgkt_2_record)
plt.title(r'$\omega$ v.s. $\theta$ $F_D$=1.15')
plt.xlabel(r'$\theta$ (radians)')
plt.ylabel(r'$\omega$ (radians/s)')
plt.scatter(rgkt_3_record[1][0],rgkt_3_record[1][1],s=1)
plt.subplot(232)
A = solving_ode.ode(3*np.pi/100,0,20000,(0.2,0))  
A.set_fx(('w','-np.sin(x)-0.5*w+1.17*np.sin(2./3*t)'),['t','x','w'])
rgkt_2_record = A.rgkt_2()[:]
rgkt_3_record = select(rgkt_2_record)
plt.title(r'$\omega$ v.s. $\theta$ $F_D$=1.17')
plt.xlabel(r'$\theta$ (radians)')
plt.ylabel(r'$\omega$ (radians/s)')
plt.scatter(rgkt_3_record[1][0],rgkt_3_record[1][1],s=1)
plt.subplot(233)
A = solving_ode.ode(3*np.pi/100,0,20000,(0.2,0))  
A.set_fx(('w','-np.sin(x)-0.5*w+1.19*np.sin(2./3*t)'),['t','x','w'])
rgkt_2_record = A.rgkt_2()[:]
rgkt_3_record = select(rgkt_2_record)
plt.title(r'$\omega$ v.s. $\theta$ $F_D$=1.19')
plt.xlabel(r'$\theta$ (radians)')
plt.ylabel(r'$\omega$ (radians/s)')
plt.scatter(rgkt_3_record[1][0],rgkt_3_record[1][1],s=1)
plt.subplot(234)
A = solving_ode.ode(3*np.pi/100,0,20000,(0.2,0))  
A.set_fx(('w','-np.sin(x)-0.5*w+1.21*np.sin(2./3*t)'),['t','x','w'])
rgkt_2_record = A.rgkt_2()[:]
rgkt_3_record = select(rgkt_2_record)
plt.title(r'$\omega$ v.s. $\theta$ $F_D$=1.21')
plt.xlabel(r'$\theta$ (radians)')
plt.ylabel(r'$\omega$ (radians/s)')
plt.scatter(rgkt_3_record[1][0],rgkt_3_record[1][1],s=1)
plt.subplot(235)
A = solving_ode.ode(3*np.pi/100,0,20000,(0.2,0))  
A.set_fx(('w','-np.sin(x)-0.5*w+1.23*np.sin(2./3*t)'),['t','x','w'])
rgkt_2_record = A.rgkt_2()[:]
rgkt_3_record = select(rgkt_2_record)
plt.title(r'$\omega$ v.s. $\theta$ $F_D$=1.23')
plt.xlabel(r'$\theta$ (radians)')
plt.ylabel(r'$\omega$ (radians/s)')
plt.scatter(rgkt_3_record[1][0],rgkt_3_record[1][1],s=1)
plt.subplot(236)
A = solving_ode.ode(3*np.pi/100,0,20000,(0.2,0))  
A.set_fx(('w','-np.sin(x)-0.5*w+1.25*np.sin(2./3*t)'),['t','x','w'])
rgkt_2_record = A.rgkt_2()[:]
rgkt_3_record = select(rgkt_2_record)
plt.title(r'$\omega$ v.s. $\theta$ $F_D$=1.25')
plt.xlabel(r'$\theta$ (radians)')
plt.ylabel(r'$\omega$ (radians/s)')
plt.scatter(rgkt_3_record[1][0],rgkt_3_record[1][1],s=1)'''
## ----------------------------------------------------
## ------------------- delta-frequency ----------------
'''A = solving_ode.ode(3*np.pi/100,0,100000,(0.2,0))  
A.set_fx(('w','-np.sin(x)-0.5*w+1.2*np.sin(2./3*t)'),['t','x','w'])
rgkt_3_record = select(A.rgkt_2(),3*np.pi)[:]
plt.subplot(131)
plt.xlabel('Theta(radians)')
plt.ylabel('Angular velocity (radians/s)')
plt.scatter(rgkt_3_record[1][0],rgkt_3_record[1][1],s=1,label = r'$\Omega_D$'+'=2/3')
plt.legend(loc = 'upper right')
A = solving_ode.ode(((2*np.pi/(2.01/3)))/100,0,100000,(0.2,0))  
A.set_fx(('w','-np.sin(x)-0.5*w+1.2*np.sin(2.01/3*t)'),['t','x','w'])
rgkt_3_record = select(A.rgkt_2(),(2*np.pi/(2.01/3)))[:]
#rgkt_3_record = A.rgkt_2()[:]
plt.subplot(133)
plt.xlabel('Theta(radians)')
plt.ylabel('Angular velocity (radians/s)')
plt.scatter(rgkt_3_record[1][0],rgkt_3_record[1][1],s=1,label = r'$\Omega_D$'+'=2.01/3')
plt.legend(loc = 'upper right')'''
'''plt.subplot(231)
A = solving_ode.ode((2*np.pi/(1.95/3))/100,0,20000,(0.2,0))  
A.set_fx(('w','-np.sin(x)-0.5*w+1.20*np.sin(1.95/3*t)'),['t','x','w'])
rgkt_2_record = A.rgkt_2()[:]
rgkt_3_record = select(rgkt_2_record,(2*np.pi/(1.95/3)))
plt.title(r'$\omega$ v.s. $\theta$ $\Omega_D$=1.95/3')
plt.xlabel(r'$\theta$ (radians)')
plt.ylabel(r'$\omega$ (radians/s)')
plt.scatter(rgkt_3_record[1][0],rgkt_3_record[1][1],s=1)
plt.subplot(232)
A = solving_ode.ode((2*np.pi/(1.97/3))/100,0,20000,(0.2,0))  
A.set_fx(('w','-np.sin(x)-0.5*w+1.20*np.sin(1.97/3*t)'),['t','x','w'])
rgkt_2_record = A.rgkt_2()[:]
rgkt_3_record = select(rgkt_2_record,(2*np.pi/(1.97/3)))
plt.title(r'$\omega$ v.s. $\theta$ $\Omega_D$=1.97/3')
plt.xlabel(r'$\theta$ (radians)')
plt.ylabel(r'$\omega$ (radians/s)')
plt.scatter(rgkt_3_record[1][0],rgkt_3_record[1][1],s=1)
plt.subplot(233)
A = solving_ode.ode((2*np.pi/(1.99/3))/100,0,20000,(0.2,0))  
A.set_fx(('w','-np.sin(x)-0.5*w+1.20*np.sin(1.99/3*t)'),['t','x','w'])
rgkt_2_record = A.rgkt_2()[:]
rgkt_3_record = select(rgkt_2_record,(2*np.pi/(1.99/3)))
plt.title(r'$\omega$ v.s. $\theta$ $\Omega_D$=1.99/3')
plt.xlabel(r'$\theta$ (radians)')
plt.ylabel(r'$\omega$ (radians/s)')
plt.scatter(rgkt_3_record[1][0],rgkt_3_record[1][1],s=1)
plt.subplot(234)
A = solving_ode.ode((2*np.pi/(2.01/3))/100,0,20000,(0.2,0))  
A.set_fx(('w','-np.sin(x)-0.5*w+1.20*np.sin(2.01/3*t)'),['t','x','w'])
rgkt_2_record = A.rgkt_2()[:]
rgkt_3_record = select(rgkt_2_record,(2*np.pi/(2.01/3)))
plt.title(r'$\omega$ v.s. $\theta$ $\Omega_D$=2.01/3')
plt.xlabel(r'$\theta$ (radians)')
plt.ylabel(r'$\omega$ (radians/s)')
plt.scatter(rgkt_3_record[1][0],rgkt_3_record[1][1],s=1)
plt.subplot(235)
A = solving_ode.ode((2*np.pi/(2.03/3))/100,0,20000,(0.2,0))  
A.set_fx(('w','-np.sin(x)-0.5*w+1.20*np.sin(2.03/3*t)'),['t','x','w'])
rgkt_2_record = A.rgkt_2()[:]
rgkt_3_record = select(rgkt_2_record,(2*np.pi/(2.03/3)))
plt.title(r'$\omega$ v.s. $\theta$ $\Omega_D$=2.03/3')
plt.xlabel(r'$\theta$ (radians)')
plt.ylabel(r'$\omega$ (radians/s)')
plt.scatter(rgkt_3_record[1][0],rgkt_3_record[1][1],s=1)
plt.subplot(236)
A = solving_ode.ode((2*np.pi/(2.05/3))/100,0,20000,(0.2,0))  
A.set_fx(('w','-np.sin(x)-0.5*w+1.20*np.sin(2.05/3*t)'),['t','x','w'])
rgkt_2_record = A.rgkt_2()[:]
rgkt_3_record = select(rgkt_2_record,(2*np.pi/(2.05/3)))
plt.title(r'$\omega$ v.s. $\theta$ $\Omega_D$=2.05/3')
plt.xlabel(r'$\theta$ (radians)')
plt.ylabel(r'$\omega$ (radians/s)')
plt.scatter(rgkt_3_record[1][0],rgkt_3_record[1][1],s=1)'''
#plt.savefig('chapter3_3.16_fre_1.png',dpi = 256)
#plt.show()
##  --------------- Vpython ---------------------
V = harmonic(0.04,0,1000,0.2)
V.calculate()
V.vplot()