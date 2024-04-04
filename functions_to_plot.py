# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:27:29 2024

@author: romas
"""

import numpy as np

# function analysis available here: https://colab.research.google.com/drive/1wVnLSEMSgwS4JGi2FpdFIeaMvfU8zvpt

def func_0():
    
    x = np.arange(-5, 7, 0.1)    
    
    label = "$y = x^3/3-2*x^2+3*x+5/3$"
  
    max_point = 1
    
    f_max = max_point**3/3-2*max_point**2+3*max_point+5/3
    
    min_point = 3
    
    f_min = min_point**3/3-2*min_point**2+3*min_point+5/3
    
    title = f"$increasing: (-\infty;{max_point}) \cup ({min_point};+\infty) \ \ decreasing: ({max_point};{min_point})$"
    
    return x, x**3/3-2*x**2+3*x+5/3, label, title, {'x': max_point, 'y': f_max}, {'x': min_point, 'y': f_min}

def func_1():
    
    x = np.arange(-10, 10, 0.1)    
    
    label = "$y = (x^2)^{1/3}$"
    
    max_point = None
    
    f_max = None
    
    min_point = 0
    
    f_min = (min_point**2)**(1/3)
    
    title = f"$decreasing: (-\infty;{min_point}) \ \ increasing: ({min_point};+\infty)$"
    
    return x, (x**2)**(1/3), label, title, {'x': max_point, 'y': f_max}, {'x': min_point, 'y': f_min}

def func_2():
    
    x = np.arange(-10, 10, 0.1)    
    
    label = "$y = x+36x^2-2x^3-x^4$"
    
    max_point = -5.0526, 3.566549
    
    f_max = max_point[0]+36*max_point[0]**2-2*max_point[0]**3-max_point[0]**4, max_point[1]+36*max_point[1]**2-2*max_point[1]**3-max_point[1]**4
    
    min_point = -0.01387
    
    f_min = min_point+36*min_point**2-2*min_point**3-min_point**4
    
    title = f"$decreasing: ({max_point[0]};{min_point}) \cup ({max_point[1]};+\infty) \ \ increasing: (\infty;{max_point[0]}) \cup ({min_point};{max_point[1]})$"
    
    return x, x+36*x**2-2*x**3-x**4, label, title, {'x': max_point, 'y': f_max}, {'x': min_point, 'y': f_min}

def func_3():
    
    x = np.arange(-4, 2, 0.1)    
    
    label = "$y = (x+1)^4+e^x$"
    
    title = "$0$"
    
    max_point = None
    
    f_max = None
    
    min_point = -1.3956
    
    f_min = (min_point+1)**4+np.exp(min_point)
    
    title = f"$decreasing: (-\infty;{min_point}) \ \ increasing: ({min_point};+\infty)$"
    
    return x, (x+1)**4+np.exp(x), label, title, {'x': max_point, 'y': f_max}, {'x': min_point, 'y': f_min}