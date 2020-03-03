import requests
import pandas as pd

from bs4         import BeautifulSoup
from selenium    import webdriver

driver = webdriver.Chrome()

req = requests.get('https://www.onul-hoi.com/m/new_welcome')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

category = soup.findAll('li',{"class":"category"})

category_list = []
page_list = []
image_list = []
rate_list = []
detail_list2 = []

#form main page, get category name and url
for i in range(3,14):
    category_list.append(
        {
            'name' : category[i].find('a').text,
            'url'  : category[i].find('a')['href']
        }
    )
#print(category_list)

#from each category, get product detail urls, name, price
for url in category_list:
    req = requests.get(url['url'])
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    urls = soup.findAll("a", {"class": "d-block"})

    for page in urls:
        try:
            address = 'https://www.onul-hoi.com'+page['href']
            page_list.append(
                {
                 'address': address,
                 'name'   : page.find('h1').text,
                 'price'  : page.find('span').text
                }
            )
        except:
             pass

#print(page_list)

#get product detail
for url in page_list:
#url
#    print(url['address'])
    driver.get(url['address'])
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # req = requests.get(url['address'])
    # html = req.text
    # soup = BeautifulSoup(html, 'html.parser')

#image
    images = soup.findAll('img')
    for image in images:
        try:
            image_list.append(image['src'])
        except:
            pass

#tagline
    tagline = soup.select(
        '#store_packages > div.productShowHeaderContent > p'
    )
#    print(tagline[0].text)

#name
    name = soup.select(
        '#store_packages > div.productShowHeaderContent > h1'
    )
#    print(name[0].text)

#price
    price = url['price']
#    print(price)

#rate
    rate = soup.select(
        '#store_packages > div.productShowHeaderContent > div > dl.average_rate > dd'
    )
    try:
        rate_list.append(rate[0].text)
    except:
        pass
#상품단위
    unit = soup.select(
        '#store_packages > div.productShowHeaderContent > dl:nth-child(5) > dd'
    )
#    print(unit[0].text)
#상품구성
    package = soup.select(
        '#store_packages > div.productShowHeaderContent > dl:nth-child(6) > dd'
    )
#    print(package[0].text)
#원산지
    origin = soup.select(
        '#store_packages > div.productShowHeaderContent > dl:nth-child(7) > dd'
    )
#    print(origin[0].text)

#배송구분
    delivery = soup.select(
        '#store_packages > div.productShowHeaderContent > dl:nth-child(8) > dd'
    )
#    print(delivery[0].text)
#주의사항
    caution = soup.select(
        '#store_packages > div.productShowHeaderContent > dl.caution'
    )
#    print(caution[0].text)

#상세페이지
    detail = soup.select('#storeDetailsContent > div.external-content')
#    print(detail)

    for item in tagline:
         detail_list2.append(
            {
                'address'  : url['address'],
                'tagline'     : item.text,
            }
        )
#print(detail_list)

data = pd.DataFrame(detail_list2)
data.to_csv('detail_list2.csv')
