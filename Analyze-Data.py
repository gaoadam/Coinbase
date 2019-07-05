# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 23:41:13 2019

@author: adamq

~~~Description~~~

This file serves to read cryptocurrency pricing data from Excel and
to analyze the data using quantitative operations.

Edit the value of time_duration to choose the duration of the data. The possible
values are 'hour', 'day', 'week', 'month', 'year', or 'all'

Edit the value of foldername to specify which folder is to be read. The folder
must first be created from scraped data by Scrape-Coinbase.py

Quantitative operations performed:

"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

"""
Data parameters
"""
#specify over how long we wish the data to take place
time_duration = 'day'
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