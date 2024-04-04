# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:27:29 2024

@author: romas
"""

import numpy as np

def func_0():
    
    x = np.arange(-10, 10, 0.1)    
    
    label = "$0$"
    
    title = "$y = x**3/3-2*x**2+3*x+5/3$"
    
    return x, x**3/3-2*x**2+3*x+5/3, label, title

def func_1():
    
    x = np.arange(-10, 10, 0.1)    
    
    label = "$0$"
    
    title = "$y = (x^2)^(1/3)$"
    
    return x, (x**2)**(1/3), label, title

def func_2():
    
    x = np.arange(-10, 10, 0.1)    
    
    label = "$0$"
    
    title = "$y = x+36x^2-2x^3-x^4$"
    
    return x, x+36*x**2-2*x**3-x**4, label, title

def func_3():
    
    x = np.arange(-10, 10, 0.1)    
    
    label = "$0$"
    
    title = "$y = (x+1)^4+e^x$"
    
    return x, (x+1)**4+np.exp(x), label, title