# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:27:17 2024

@author: romas
"""


import matplotlib.pyplot as plt

import numpy as np


class DataContainer:
 
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def plot(self, fig=None, ax=None, title = "My preferred title", text="ОВ", **kwargs):
        
        if fig is None:
            
            fig = plt.gcf()
            
        if ax is None:
            
            ax = plt.gca()
            
        # при передачі **kwargs в функцію plot відбувається розпакування key, value зі словника
        print('Надрукуємо словник kwargs', kwargs)
        
        print()
        
        x_asymptote = kwargs.pop("x_asymptote", None)

        y_asymptote = kwargs.pop("y_asymptote", None)
        
        obl_asymptote = kwargs.pop("obl_asymptote", None)
        
        maximal = kwargs.pop("maximal", None)

        minimal = kwargs.pop("minimal", None)
        
        plot_num = kwargs.pop("plot_num", None)
        
        self.y[:-1][np.abs(np.diff(self.y)) > 20] = np.nan
        
        if y_asymptote is not None:

          # horizontal asymptote
          for y_as in y_asymptote:

               ax.axhline(y=y_as, color="red", linestyle="--")
          
               ax.plot(self.x, np.ma.masked_where(self.y > y_as, self.y), **kwargs)
               ax.plot(self.x, np.ma.masked_where(self.y < y_as, self.y), **kwargs)
        
        if x_asymptote is not None:
            
            # vertical asymptote
            for x_as in x_asymptote:
                
                ax.axvline(x=x_as, color="red", linestyle="--")
                
                if y_asymptote[0] is None:
                    
                    ax.plot(self.x, np.ma.masked_where(self.x > x_as-0.01, self.y), **kwargs)
                    ax.plot(self.x, np.ma.masked_where(self.x < x_as+0.01, self.y), **kwargs)
                    
        elif x_asymptote is None and y_asymptote is None:
             
             ax.plot(self.x, self.y, **kwargs)
 
        if obl_asymptote is not None:

            ax.axline((obl_asymptote[0],obl_asymptote[1]), slope=obl_asymptote[2], color="red", linestyle="--")
        
    
        ax.set_xlabel('x', fontsize=12)
        
        ax.set_ylabel('y', fontsize=12)
        
        ax.set_title(title)
        
        x_i = -1
        
        a = self.x[x_i]/2
        
        while np.isnan(a):
            
            a = self.x[x_i]/2
            
            x_i -= 1
            
        y_i = 1
        
        b = self.y[y_i]
        
        while np.isnan(b):
            
            b = self.y[y_i]
            
            y_i += 1
            
        y_lim_bottom = min(self.y)-2
        
        y_lim_top = max(self.y)+2
        
        
        
        if np.isnan(y_lim_bottom):
            
            y_lim_bottom = -20
            
        if np.isnan(y_lim_top):
            
            y_lim_top = 600
            
        y_lim_len = abs(y_lim_bottom) + abs(y_lim_top)  
        
        if abs(y_lim_bottom) < y_lim_len/10:
            
            add_step = y_lim_len/5
            
            y_lim_bottom -= y_lim_len/3
            
        else:
            
            add_step = 0
        
        if None not in maximal.values():
            
            max_x, max_y = maximal.get('x'), maximal.get('y')
            
            if type(max_x) == int or type(max_x) == float:
                
                ax.scatter(max_x, max_y)
    
                ax.annotate(f'max: ({max_x},{max_y})', xy=(max_x, max_y), xytext=(max_x, max_y-(abs(y_lim_bottom)+add_step)/2),
                    arrowprops = dict(facecolor = 'black', shrink=1.00, headwidth = 3.5, width = 0.1))
                
            else:
            
                for x_val, y_val in zip(max_x, max_y):
                    
                    ax.scatter(x_val, y_val)
        
                    ax.annotate(f'max: ({x_val},{y_val})', xy=(x_val, y_val), xytext=(x_val, y_val-(abs(y_lim_bottom)+add_step)/2),
                        arrowprops = dict(facecolor = 'black', shrink=1.00, headwidth = 3.5, width = 0.1))
       
        if None not in minimal.values():
 
            min_x, min_y = minimal.get('x'), minimal.get('y')
            
            if type(min_x) == int or type(min_x) == float:
                
                
                
                ax.scatter(min_x, min_y)
    
                ax.annotate(f'min: ({min_x},{min_y})', xy=(min_x, min_y), xytext=(min_x, min_y-(abs(y_lim_bottom)+add_step)/2),
                    arrowprops = dict(facecolor = 'black', shrink=1.00, headwidth = 3.5, width = 0.1))
            else:
                
                for x_val, y_val in zip(min_x, min_y):
                    
                    ax.scatter(x_val, y_val)
        
                    ax.annotate(f'min: ({x_val},{y_val})', xy=(x_val, y_val), xytext=(x_val, y_val-(abs(y_lim_bottom)+add_step)/2),
                        arrowprops = dict(facecolor = 'black', shrink=1.00, headwidth = 3.5, width = 0.1))
            
        ax.legend()
        
        ax.set_ylim(y_lim_bottom, y_lim_top)
        
        ax.grid(True)
        
        plt.savefig(f'saved_figures/func_{plot_num}.png')
        
        return ax