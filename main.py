# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 22:56:33 2024

@author: romas
"""

import functions_to_plot as ftp

import data_container_class as dcc

import inspect as insp

import matplotlib.pyplot as plt

import math as m


def fill_arr(array: list, to_be_plotted: list):
    
    if len(array) < len(to_be_plotted):
        
        elms_to_add_num = abs(len(array)-len(to_be_plotted))
        
        if len(array) < m.floor(len(to_be_plotted)/2):
            
            multiple = (m.floor(len(to_be_plotted)/2*len(array))) 
            
            array = array*multiple
        
        elms_to_add = array[:elms_to_add_num]
        
        new_array = [elm for elm in array + elms_to_add]
        
    else:
        
        new_array = array
        
    return new_array

def plot_func_on_1_1_mosaic(to_be_plotted: list, colors: list, markers: list, 
                            linewidth: float, marker_size: int) -> tuple:

    fig, axs = plt.subplot_mosaic([['upper'],
                                    ['lower']],
                                    figsize = (5.5, 3.5), layout = 'constrained')
    
    for axis, func, color, marker, linestyle in zip(axs.values(), to_be_plotted, colors, markers, linestyles):
        
        x, y, label, title, maximal, minimal = func[1]()
        
        data = dcc.DataContainer(x, y)
        
        data.plot(fig=fig, ax=axis, color=color, marker=marker, linestyle=linestyle, linewidth=linewidth, 
                  markersize=marker_size, label=label, title=title, 
                  maximal = maximal, minimal = minimal)
    
        linewidth += 0.1
        
        marker_size += 1
        
    plt.show()  
     
    return linewidth, marker_size

colors = ['green', 'darkcyan', 'blue', 'magenta', 'red', 'purple', 'orange']

markers = ['o', '^', '.', ',', 'v', '>', '<', '1', '2', '3']

linestyles = ['solid', 'dotted', 'dashed', 'dashdot']

linewidth, marker_size = 1.0, 0

to_be_plotted = insp.getmembers(ftp, insp.isfunction)

colors = fill_arr(colors, to_be_plotted)

markers = fill_arr(markers, to_be_plotted)

linestyles = fill_arr(linestyles, to_be_plotted)

print()

for i, func, color, marker, linestyle in zip(dict(enumerate(to_be_plotted)).keys(), to_be_plotted, colors, markers, linestyles):
    
    x, y, label, title, maximal, minimal = func[1]()
    
    data = dcc.DataContainer(x, y)
    
    fig, axis = plt.subplots(1, 1, layout="constrained", figsize=(10,6))
    
    data.plot(fig=fig, ax=axis, color=color, marker=marker, linestyle=linestyle, linewidth=linewidth, 
              markersize=marker_size, label=label, title=title, maximal = maximal, minimal = minimal, plot_num = i)

    plt.show()
    
    linewidth += 0.1
    
    marker_size += 1
     