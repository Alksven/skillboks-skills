import requests
from bs4 import BeautifulSoup


website = requests.get('http://www.columbia.edu/~fdc/sample.html')
html = website.content
soup = BeautifulSoup(html, 'html.parser')

texts = [p.text for p in soup.find_all('h3')]
print(texts)
