#scraper for python
from bs4 import BeautifulSoup
from lxml import etree
import requests

items=['https://www.sephora.ae/en/p/glowscreen-sunscreen-spf-30-with-hyaluronic-acid-%2B-niacinamide-P10049094.html',
       'https://www.sephora.ae/en/p/soft-pinch-liquid-blush-P10017094.html',
       'https://www.sephora.ae/en/p/honey-infused-hair-oil-P10014606.html',
       'https://www.sephora.ae/en/p/airwrap%E2%84%A2-multi-styler-and-dryer-in-ceramic-pink-and-rose-gold-P10057417.html']

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    'Accept': '/', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
}
#def scrape_price(link):
link = 'https://www.sephora.ae/en/p/honey-infused-hair-oil-P10014606.html'
htmlResponse = requests.get(link,headers=header)
#price = link.xpath('/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/div[4]/div[2]/div/div[1]/span')
#price = price.replace(" AED","")
#print(int(price))
bs=BeautifulSoup(htmlResponse.content,'lxml')
xyz=etree.HTML(str(bs))
element=xyz.xpath('//*[@id="product-content"]/div[2]/div/div[1]/span')
print (element[0].text)
price=element[0].text
price = price.replace(" AED","")
print(float(price))

#poa: make object for price, name, description



