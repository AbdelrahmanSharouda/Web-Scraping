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
#print(soup)

for a in soup.findAll('a', href=True, attrs={'class': '_1fQZEK'}):
    name = a.find('div', attrs={'class': '_4rR01T'})
    print(name)
    price = a.find('div', attrs={'class': '_30jeq3 _1_WHN1'})
    print(price)
    rating = a.find('div', attrs={'class': '_3LWZlK'})
    print(rating)
    product.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)

df = pd.DataFrame({'Product Name': product, 'Price': prices, 'Rating': ratings})
df.to_csv('products2.csv', index=False, encoding='utf-8')
