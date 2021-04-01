import requests
from bs4 import BeautifulSoup as bs

url = 'https://quotes.toscrape.com'
news_response = requests.get(url)
html = news_response.text

soup_div = bs(html,'html.parser')


filter_by = {
    'class':'text'
}
values = []
for tag_Data in soup_div.findAll('span',filter_by):
    data=tag_Data.string
    values.append(data.replace('“','').replace('”',''))
print(values)


dicts = {}
keys = range(len(values))

for i in keys:
        dicts[i] = values[i]
print(dicts)