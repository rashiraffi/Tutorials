# Refrence https://www.edureka.co/blog/web-scraping-with-python/
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

def removespan(span):
    #span=str(span)
    print(span)
    print(span.index('</'))
    #span=span[:int(span.index("</span>"))]
    return span

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

driver.get("https://google.com/covid19-map/?hl=en")

content = driver.page_source
soup = BeautifulSoup(content)
country=dict()
for a in soup.findAll('tr', attrs={'class':'A5V3jc'}):
    name=a.find('span')
    name=removespan(name)
    print(name)
    #price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    #rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
    #products.append(name.text)
    #prices.append(price.text)
    #ratings.append(rating.text)