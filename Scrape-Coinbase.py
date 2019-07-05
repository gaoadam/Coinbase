# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 16:59:52 2019

@author: adamq


~~~~Description~~~~

This file serves to scrape cryptocurrency pricing data over time from
coinbase.com/prices

This file creates a folder named after the date and time during which it was
run. Multiple Excel files are saved into the folder, one for each cryptocurrency.
"""

import json
import pandas as pd
import requests
import datetime
import os
from bs4 import BeautifulSoup


url = 'https://www.coinbase.com/price'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#Scrape urls leading to cryptocoin prices
tdTags = soup.find_all("td", class_="AssetTableRow__Td-sc-1e35vph-1 RYZCE")
aTags = []
for tag in tdTags:
    aTag = tag.find_all('a')
    aTags += aTag
    
#Scrape each url for pricing data
homeurl = 'https://www.coinbase.com'
scriptTags = []

for i in range(0, len(aTags)):
    link = aTags[i]['href']
    fullurl = homeurl + link
    print("Scraping from: " + fullurl)
    
    page = requests.get(fullurl)
    soup2 = BeautifulSoup(page.content, 'html.parser')

    #scrape coin price from plot
    scriptTag = soup2.find_all("script", {'id' : 'server-app-state'})
    scriptTags += scriptTag

index = [i for i in range(0, len(aTags))]
names = []
currencies = []

#Get current time
currenttime = datetime.datetime.now()

#Name the folder in which files will be saved
foldername = str(currenttime.year) + "-" + str(currenttime.month) + "-" + \
                 str(currenttime.day) + "-" + str(currenttime.hour) + "-" + \
                 str(currenttime.minute) + "-" + str(currenttime.second)

#Print time to text file:
                 
path = os.getcwd() + "\\" +foldername + "\\"
os.makedirs(path)

with open(path + "datetime.txt", mode='w') as file:
    file.write(str(currenttime))
    

#Name 
#Extract data from scriptTags
for i in range(0, len(scriptTags)):
    #Convert javascript item text into dictionary with accesssible keys
    #Extract cryptocurrency name and cryptocurrency prices per hour/day/week
    data = json.loads(scriptTags[i].text)
    
    #cryptocurrency name
    name = data['data']['asset']['name']
    currency = data['storeData']['localeInfo']['currency']
    prices = data['data']['prices']
    
    names += [name]
    currencies += [currency]
    
    #Make data type of prices usable/plottable using pandas
    #time is in units of 1000 seconds
    
    print("Converting to Excel: " + name)
    
    # ~~~~Save pandas files to Excel format~~~~
    
    path = os.getcwd() + "\\" + foldername + "\\"
    writer = pd.ExcelWriter(path=path + str(i) + '-' + name + '.xlsx', engine='xlsxwriter')
    
    for j in range(0, len(prices)):
        time_length = prices[j][0]
        df = pd.DataFrame(prices[j][1])
        
        df.to_excel(excel_writer = writer, sheet_name = time_length)
        

#Save file names to text file
fnames = []
for i in range(0, len(names)):
    fnames += [str(i) + '-' + names[i]]
    
row_data = list(zip(fnames, currencies))

path = os.getcwd() + "\\" +foldername + "\\"
with open(path + "filenames.txt", mode='w') as file:
    for i in range(0, len(fnames)):
        file.write(str(row_data[i])+"\n")
    
