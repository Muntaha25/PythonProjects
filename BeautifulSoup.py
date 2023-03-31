from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.previewochomes.com/laguna-beach.php?p=2#grid"
page = requests.get(url)


soup = BeautifulSoup(page.text, 'html.parser')
listings = soup.find_all('div', class_="uk-width-small-1-1")
 

with open('preview.csv', 'w', encoding = 'utf8', newline='') as f:

  thewriter = writer(f)
  header=['Office', 'Agent', 'Address', 'Price']
  thewriter.writerow(header)


  for lists in listings:
        

        Office = lists.find('span', class_="office")
        Agent = lists.find ('span', class_="agent")
        Address = lists.find('h4')
        Price = lists.find('span')



        info = [Office, Agent, Address, Price]
       # print(info)
        thewriter.writerow(info)