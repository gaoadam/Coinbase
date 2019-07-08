# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 00:36:19 2019

@author: adamq


~~~~Description~~~~

This file serves to read cryptocurrency pricing data from Excel and
to output plots of their raw pricing in png form.

Edit the value of time_duration to choose the duration of the data. The possible
values are 'hour', 'day', 'week', 'month', 'year', or 'all'

Edit the value of foldername to specify which folder is to be read. The folder
must first be created from scraped data by Scrape-Coinbase.py

"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

"""
Data parameters
"""
#specify over how long we wish the data to take place
time_duration = 'year'
time_unit = 1000

"""
Extract data from Excel format to pandas DataFrame format
"""

"""
~~~~~~~~SPECIFY FOLDER NAME HERE~~~~~~~~~~~~~
"""
#Folder Name:
foldername = '2019-7-4-22-47-35'

#Folder path
path_load = os.getcwd() + "\\" + foldername + "\\"

#Get names of Excel files
xlfilenames = open(path_load + 'filenames.txt', mode='r')

#Change directory to be saved in
path_home = os.getcwd() + "\\" +foldername + "-analysis" + "\\"
path_plot = path_home + "plots-" + time_duration + "\\"
if not os.path.exists(path_plot):
    os.makedirs(path_plot)
    

for row in xlfilenames:
    row = eval(row.strip('\n'))
    xlfilename, currency = row
    df = pd.read_excel(path_load + xlfilename + '.xlsx', time_duration)
    print('reading ' + xlfilename)
    
    #Adjust time into seconds
    df['time'] = (df['time'] - df['time'][0])/time_unit
    
    
    """
    ~~~~~Plot~~~~~
    """
    
    #File name and Title name of plot
    plotfilename = xlfilename + '-plot-' + time_duration
    plot_title = xlfilename + ', ' + currency + ', past ' + time_duration + ', ' + str(len(df['time'])) + ' samples'
    
    #Determine length and units of ticks on plot
    length_minute = 60
    length_hour = 60*60
    length_day = 24*60*60
    
    if time_duration == 'hour':
        length_tick = 5*length_minute
        unit_tick = length_minute
        xunit = 'minutes'
    elif time_duration == 'day':
        length_tick = length_hour
        unit_tick = length_hour
        xunit = 'hours'
    elif time_duration == 'week':
        length_tick = length_day
        unit_tick = length_day
        xunit = 'days'    
    elif time_duration == 'month':
        length_tick = 2*length_day
        unit_tick = length_day
        xunit = 'days'
    elif time_duration == 'year':
        length_tick = 30*length_day
        unit_tick = length_day
        xunit = 'days'
    elif time_duration == 'all':
        length_tick = 200*length_day
        unit_tick = length_day
        xunit = 'days'
    
    #convert units of time to unit_ticks
    df['time'] = df['time']/unit_tick
    
    #Create the actual plot object and save it
    ax = df.plot(x='time', y='price')
    fig = ax.get_figure()
    plt.legend(['price, ' + currency])
    plt.title(plot_title)
    plt.xlabel('time, ' + xunit)
    plt.xticks(np.arange(0, int(df['time'][len(df['time'])-1])+1, length_tick/unit_tick))
    plt.savefig(path_plot + plotfilename + '.png')
    plt.close(fig)
    
    
    
    