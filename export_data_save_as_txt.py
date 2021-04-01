import requests
from bs4 import BeautifulSoup as bs

url = 'https://quotes.toscrape.com'
news_response = requests.get(url)
html = news_response.text
soup_div = bs(html,'html.parser')
filter_by = {
    'class':'text'
}

with open('soup_export_quats.txt','w') as f:
    for tag_Data in soup_div.findAll('span',filter_by):
        data=tag_Data.string
        value =data.replace('“','').replace('”','')
        print(value)
        f.write(value)
        f.write('\n')
