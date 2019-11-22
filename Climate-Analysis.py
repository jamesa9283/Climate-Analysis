# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 11:16:20 2019

@author: james
"""

import numpy as np
import matplotlib.pyplot as plt


def Fig(src, name):
    """
    A function that plots data from a csv and outputs a graph
    Input: src: A CSV file that is in the working directory
           name: The name of the output file
    Output: The figure, also saved to your working directory
    """
    data = np.genfromtxt(src, delimiter=',', dtype=None, skip_header=1, names=('year', 'month', 'tmax', 'tmin', 'AirFrost'))
        
    plt.title('Averaged Minimum Temperature per year from 1978 to 2019')
    plt.xlabel('Month')
    plt.ylabel('degrees')
    plt.bar(data['year'], data['AirFrost'], color='c')
    plt.savefig(name + ".png")
    
Fig('CBNdata.csv', 'tmin')