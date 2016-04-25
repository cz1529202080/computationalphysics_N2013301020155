# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 11:01:46 2016
@author: AF
"""

import ode as solving_ode
import matplotlib.pyplot as plt
import time

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
            self.w.append(self.w[i - 1] - self.x[i - 1]*self.dt)
            self.x.append(self.x[i - 1] + self.w[i] * self.dt)
            self.t.append(self.t[i - 1] + self.dt)
        return self.t, self.x
        
    def find_period(self):
        t_period = []
        for i in range(len(self.x)):
            if abs(self.x[i] - self.x_0) < 0.000001 and self.t[i] > 20*self.dt:
                t_period.append(self.t[i])
            else:
                pass
        s = 0
        for j in range (2):
            s = s + t_period[j]
        print "the period is:%f" %(s/2)
        return s/2
        
class harmonic_alpha3(harmonic):
    def calculate(self):
        self.w = []
        self.x = []
        self.t = []
        self.t.append(self.a)
        self.w.append(0)
        self.x.append(self.x_0)
        for i in range(1,self.N):
            self.w.append(self.w[i - 1] - self.x[i - 1]**3*self.dt)
            self.x.append(self.x[i - 1] + self.w[i] * self.dt)
            self.t.append(self.t[i - 1] + self.dt)
        return self.t, self.x
        

plt.figure(figsize = (10,6))
### --------------- forth-order Runge-Kutta ----------
#start=time.clock()
A = solving_ode.ode(0.1,0,40,(0,1.2))  
A.set_fx(('-x**5','w'),['t','w','x'])
rgkt_3_record = A.rgkt_4()[:]
#end = time.clock()
#print "read: %f s" % (end - start)
### -------------- second-order Runge-Kutta ----------
#rgkt_2_record = A.rgkt_2()[:]
### -----------------------------------------------
#start=time.clock()
B = harmonic_alpha3(0.04,0,40,1.2)
euler_c_record = B.calculate()
#B.find_period()
#end = time.clock()
#print "read: %f s" % (end - start)
### ------------- alpha = 3 ----------------------
'''amplitude = 0.8
for i in range(5):   ## 0.2 0.4 0.6 0.8 1.0
    C = harmonic_alpha3(0.01, 0, 40, amplitude)
    euler_a_record = C.calculate()
    period = C.find_period()
    plt.plot(euler_a_record[0], euler_a_record[1], label = 'Amplitude:'+str(amplitude))
    amplitude = amplitude + 0.2'''
### -----------------------------------------------
plt.plot(rgkt_3_record[0],rgkt_3_record[1][1],label = '4th-order Runge-Kutta method')
#plt.plot(rgkt_2_record[0],rgkt_2_record[1][1],label = '2nd-order Runge-Kutta method')
plt.plot(euler_c_record[0],euler_c_record[1], label = 'Euler_Cromer method')
plt.legend(loc = 'upper left')
plt.savefig('chapter3_3.4.png',dpi = 144)
plt.show()
Status API Training Shop Blog About
© 2016 GitHub, Inc. Terms Privacy Security Contact Help