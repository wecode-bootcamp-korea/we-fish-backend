import requests
import pandas as pd
from bs4 import BeautifulSoup

req  = requests.get('https://www.onul-hoi.com/m/new_welcome')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

category = soup.findAll('li',{"class":"category"})

category_list = []
page_list = []

#form main page, get category name and url
for i in range(3, 14):
    category_list.append(
        {
            'name' : category[i].find('a').text,
            'url'  : category[i].find('a')['href']
        }
    )
#print(category_list)

#from each category, get product detail urls, name, price
for url in category_list:
    req  = requests.get(url['url'])
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    urls   = soup.findAll("a", {"class": "d-block"})
    images  = soup.select(
        'a > article > div.thumbnail > img'
    )

    name   = soup.select(
        'div.productCardContent > h1'
    )

    for item in zip(urls, images, name):
        try:
            address = 'https://www.onul-hoi.com'+item[0]['href']
            page_list.append(
                {
                    'category' : url['name'],
                    'address'  : address,
                    'image'    : item[1]['src'],
                    'name'     : item[2].text,
                    'price'    : item[0].find('span').text
                }
            )
        except:
             pass

data = pd.DataFrame(page_list)
data.to_csv('page_list.csv')
