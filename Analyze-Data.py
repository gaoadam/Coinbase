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
import statsmodels.tsa.stattools as stt
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
path_plot2 = path_home + "bargraphs-" + time_duration + "\\"
if not os.path.exists(path_plot1):
    os.makedirs(path_plot1)
if not os.path.exists(path_plot2):
    os.makedirs(path_plot2)
    
#Create dataframe in which to store statisitcal analysis data
Stat_columns = ['idkey', 'currency', 'ADFstatistic', 'pvalue',
                'CriticalValue 1%', 'CriticalValue 5%', 'CriticalValue 10%',]
Statistical_Analysis = pd.DataFrame(data= [], columns = Stat_columns)


for row in xlfilenames:
    row = eval(row.strip('\n'))
    xlfilename, currency = row
    df = pd.read_excel(path_load + xlfilename + '.xlsx', time_duration)
    print('reading ' + xlfilename)
    
    #Adjust time into seconds
    df['time'] = (df['time'] - df['time'][0])/time_unit
    
    """
    
    Begin Statistical Analysis Methods
    
    """
    #Rolling Mean
    
    
    
    #Dickey-Fully Test
    #Note CriticalValues are not used in this case.
    DickeyFully = stt.adfuller(df['price'])
    ADFstatistic = DickeyFully[0]
    pvalue = DickeyFully[1]
    CriticalValues = DickeyFully[4]
    
    #Append values to Statistical_Analysis data dataframe
    idkey = xlfilename.split('-')[0]
    currency = xlfilename.split('-')[1]
    
    df_appendable = pd.DataFrame(data = [[idkey, currency, ADFstatistic, pvalue,
                                         CriticalValues['1%'], CriticalValues['5%'], CriticalValues['10%']]],
                                columns = Stat_columns)
    Statistical_Analysis = Statistical_Analysis.append(df_appendable, ignore_index=True)
"""

Plot Data and save it

"""
#Save data to csv format
Statistical_Analysis.to_csv(path_home + 'Statistical_Analysis.csv')

#Plot statistical data: ADFstatistic
ax_ADFstatistic = Statistical_Analysis.sort_values('ADFstatistic',
                                                   ascending = 'False').plot.bar(x = 'currency', y='ADFstatistic',
                                                                      figsize = (10,6))
fig = ax_ADFstatistic.get_figure()
plt.title('ADFstatistic, past ' + time_duration)
plt.tight_layout()
plt.savefig(path_plot2 + 'ADFstatistic.png')
plt.close(fig)

#Plot statistical data: pvalue
ax_pvalue = Statistical_Analysis.sort_values('ADFstatistic',
                                                   ascending = 'False').plot.bar(x = 'currency', y='pvalue',
                                                                      figsize = (10,6))
fig = ax_pvalue.get_figure()
plt.title('p-value, past ' + time_duration)
plt.tight_layout()
plt.savefig(path_plot2 + 'pvalues.png')
plt.close(fig)