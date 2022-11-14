from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

driver = webdriver.Chrome("D:\Chromedriver\chromedriver.exe")
product = []
prices = []
ratings = []

driver.get("https://www.flipkart.com/laptops/~cs-g5q3mw47a4/pr?sid=6bo%2Cb5g&collection-tab-name=Browsing&wid=13.productCard.PMU_V2_3")
content = driver.page_source
soup = BeautifulSoup(content)

for a in soup.findAll('a', href=True, attrs={'class': '_1fQZEK'}):
    name = a.find('div', attrs={'class': '_4rR01T'})
    price = a.find('div', attrs={'class': '_30jeq3 _1_WHN1'})
    rating = a.find('div', attrs={'class': '_3LWZlK'})
    product.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)

df = pd.DataFrame({'Product Name': product, 'Price': prices, 'Rating': ratings})
df.to_csv('products2.csv', index=False, encoding='utf-8')


## This is another application to the same algorithm to list college master's program.

product = []
prices = []
durationValues = []
cname = []


driver.get("https://www.mastersportal.com/search/master/data-science-big-data/germany/page-2?tr=[5000,10000],[1000,5000],[500,1000],[0,500]")
content = driver.page_source
soup = BeautifulSoup(content)
#print(soup)

for a in soup.findAll('a', href=True, attrs={'class': 'SearchStudyCard js-bestFitStudycard'}):
    name = a.find('h2', attrs={'class': 'StudyName'})
    price = a.find('div', attrs={'class': 'TuitionValue'})
    durationValue = a.find('div', attrs={'class': 'DurationValue'})
    collegename = a.find('strong', attrs={'class': 'OrganisationName'})

    product.append(name.text)
    prices.append(price.text)
    durationValues.append(durationValue.text)
    cname.append(collegename.text)

df = pd.DataFrame({'Product Name': product, 'Price': prices, 'duration': durationValues, 'College Name': cname})
df.to_csv('testt.csv', index=False, encoding='utf-8')
