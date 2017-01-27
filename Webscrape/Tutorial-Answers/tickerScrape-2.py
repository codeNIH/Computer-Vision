from bs4 import BeautifulSoup
import requests

## General Version ##

#For our purposes we will use www.nasdaq.com to retrieve the information we want
#We want to create variable that asks the user to input a ticker symbol e.g. GOOG
ticker = raw_input("Enter ticker symbol: ")

#Create a url variable that incorporates the users input
#into the web address that leads us to the webpage we want
url = 'http://www.nasdaq.com/symbol/' + ticker

#Create a response object using the get function in requests
#We will be able to get all the information we need from this object
element = requests.get(url)

#Since we are only interested in the text part of our webpage,
#we will get the text attribute of our response object
plain_text = element.text

#We will create a BeautifulSoup object that represents the webpage as a whole,
#using html.parser as our parser of choice
soupObject = BeautifulSoup(plain_text, 'html.parser')

#In order for our script to locate our text of interest, we want
#to right-click on the stock price and choose inspect
#This will reveal a hierarchy of html tags with the price highlighted
#We want to use the find function in a loop to parse through
#the html document in sections (represented by the div element)
#until we find the unique identifier for our text of interest
for tickNum in soupObject.find('div', {'id':'qwidget_lastsale'}):
        print tickNum
        
## Bonus Version ##

def bonus():
  os.system('clear') 
  choice = 'y'.lower()

  while choice == 'y':
      ticker = raw_input("Enter ticker symbol: ").upper()
      url = 'http://www.nasdaq.com/symbol/' + ticker
      element = requests.get(url)
      plain_text = element.text
      soupObject = BeautifulSoup(plain_text, 'html.parser')

      for g_data in soupObject.find_all('div', {'id':'qwidget-quote-wrap'}): 
          stock = g_data.contents[1].text
          ticknum = g_data.contents[5].find('div', {'id':'qwidget_lastsale'}).text
          time = g_data.contents[7].find('span', {'id':'qwidget_markettime'}).text
          print('\nAs of ' + time + ', the last sale for ' + stock.replace('Quote & Summary Data','') + 'was ' + ticknum + '\n')

      choice = raw_input('Search again? \n(y/n): ')
      if choice == 'n'.lower():
          os.system('exit')
        
# UNCOMMENT for Bonus version          
# bonus()
