from bs4 import BeautifulSoup
import requests

source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source,'lxml')
# print(soup.prettify())
article = soup.find('div',class_='container')
print(article)