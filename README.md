# Coinbase
In this project, I use the Python library BeautifulSoup to scrape cryptocurrency pricing data from Coinbase. I then visualize and analyze
the stationarity of the pricing using the augmented Dickey-Fuller method.

Please read 'Writeup.pdf' for a brief summary of the python files' uses and examples of how the results are visualized and analyzed.

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
