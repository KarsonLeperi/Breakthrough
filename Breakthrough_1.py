# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 12:52:53 2016

@author: Karson
"""

from scipy.integrate import ode
import math
import numpy as np

def derivative(t, y):

    N=len(y)
    y_inlet=0.1+99.9*math.exp(-0.5*t)    
    dP= np.zeros(N)
    dP[0]=y_inlet-y[0]
    dP[1:N]=y[0:N-1]-y[1:N]
    return 0.5*dP
   
def initialization(N):
    y=np.zeros(N)
    y[0:N]=100
    t=0
    return y, t
   
y0, t0 = initialization(10)

r= ode(derivative).set_integrator('vode', method='adams')
r.set_initial_value(y0, t0)
t_end=50
dt=1




while r.successful() and r.t < t_end:
    print(r.t+dt, r.integrate(r.t+dt))