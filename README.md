# Coinbase
Scrape, analyze, and visualize cryptocurrency pricing data from Coinbase

READ Writeup.pdf for a Description on how the files are used and how results are obtained/analyzed.

# File Descriptions:
##   Scrape-Coinbase.py:

  This file serves to scrape cryptocurrency pricing data over time from
  coinbase.com/prices

  This file creates a folder named after the date and time during which it was
  run. Multiple Excel files are saved into the folder, one for each cryptocurrency.
  
##   Read-Data.py

  This file serves to read cryptocurrency pricing data from Excel and
  to output plots of their raw pricing in png form.

  Edit the value of time_duration to choose the duration of the data. The possible
  values are 'hour', 'day', 'week', 'month', 'year', or 'all'

  Edit the value of foldername to specify which folder is to be read. The folder
  must first be created from scraped data by Scrape-Coinbase.py

##    Analyze-Data.py
  This file serves to read cryptocurrency pricing data from Excel and
  to analyze the data using quantitative operations.

  Edit the value of time_duration to choose the duration of the data. The possible
  values are 'hour', 'day', 'week', 'month', 'year', or 'all'

  Edit the value of foldername to specify which folder is to be read. The folder
  must first be created from scraped data by Scrape-Coinbase.py