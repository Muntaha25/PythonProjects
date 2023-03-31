#Packages' Import

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
import urllib
import json

# Pararius Scraper Class 

class Zameenscraper (scrapy.Spider):
    #naming the spider
    name= 'Zameen'

#base url
base_url= 'https://www.zameen.com/Rentals_Flats_Apartments/'

#string query parameters for pagination purpose
params = {'price_min':10000,
'price_max' :100000,
'baths_in':2,
'beds_in':3}

#custom headers

headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36'}

#custom seeting

custom_settings = {
'FEED_FORMAT': 'csv',
'FEED_URL': 'Zameen.com',

 #To limit the spider speed and productivity
'Concurrent_requests_per_domain' : 2,
'Download_delay' : 1
}

#crawler entry points

def start_requests(self):

   #loop over the page range (0,n) for pagination
   
   for page in range (1, 3):
   
      #generate next page url
      next_page = self.base_url + 'Karachi-2-' + str(page) +'.html?'
      next_page += urllib.parse.urlencode(self.params)
      
      #print(next_page)   
      #to check if all of the links are there 


# crawl the next page url
      yield scrapy.requests(url = next_page, 
headers = self.headers, 
callback = self.parse)
      break
#(after crawling the first page)

#parse property cards

def parse (self, response):
      
      
      #writer reponse to local file
 #with open ('res.html', 'w') as f:
  #     f.write(response.text)
   
   #local html content
   content = ''

       #load local html file to debug datatration logic
   with open ('res.html', 'r') as f:
    for line in f.read():
     content += line
             
             #init scrapy selector
    response = Selector(text=content)
  
   #loop over property cards data

   for card in response.css('li[role="article"]'):
     print(card.get())
   #data extraction 
    #features: { }
     
     



# main driver
if __name__ == '__main__':
 


#run scraper
 process = CrawlerProcess()
 process.crawl(Zameenscraper)
 process.start()

 Zameenscraper.parse(Zameenscraper, '')