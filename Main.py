import requests
from bs4 import BeautifulSoup
import pandas

r = requests.get("https://www.zillow.com/homes/for_sale/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-111.239189453125%2C%22east%22%3A-101.900810546875%2C%22south%22%3A31.415978650329038%2C%22north%22%3A38.7510589689832%7D%2C%22mapZoom%22%3A7%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%7D", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

c=r.content
soup=BeautifulSoup(c,"html.parser")
#print(soup.prettify())

all=soup.find_all("article",{"class":"list-card list-card_not-saved"})

l = []
for i in all:
    d = {}
    try:
        d['Address'] = i.find('div',{'class','list-card-info'}).find('address').text
    except:
        d['Address'] = None
    try:
        d['Price'] = i.find('div', {'class', 'list-card-price'}).text
    except:
        d['Price'] = None
    try:
        d['Bedrooms'] = i('li')[0].text 
    except:
        d['Bedrooms'] = None
    try:
        d['Bathrooms'] = i('li')[1].text
    except:
        d['Bathrooms'] = None
    try:
        d['Square Feet'] = i('li')[2].text
    except:
        d['Square Feet'] = None
        
    l.append(d)
        
   # print(l)

    
df = pandas.DataFrame(l)

df.head(50)
