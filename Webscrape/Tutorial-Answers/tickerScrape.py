## Objective
# 1. Prompt user to enter a TICKER symbol
# 2. Use provided TICKER to scrape appropriate Yahoo Finance page
# 3. Use Beautiful Soup Package to retrieve current price for one share of stock, of specified company
# 4. Print value to the console

import requests
from bs4 import BeautifulSoup

# This function works in Python 2.x NOT Python 3.x
TICKER = raw_input("Please enter the ticker symbol: ")

# Replaces ticker symbol in the URL to provide dynamic site access
URL = "http://finance.yahoo.com/quote/" + TICKER + "?p=" + TICKER

# Pings requested site for content; HTTPS response code is actually embedded in 'element'
element = requests.get(URL)

# Displays text within content
plaintext = element.text

# Initialize a BeautifulSoup Object; represents HTML of URL as a nested data structure (Ready for our parsing :) )
soupObject = BeautifulSoup(plaintext, 'html.parser')

# Searches source code for specified class (looks like gibberish); but it contains our share value
for item in soupObject.findAll("span", {"class":"Fw(b) Fz(36px) Mb(-4px)"}):
  # Print the text within this specified span class
  print item.text
