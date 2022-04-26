import requests, csv
from bs4 import BeautifulSoup

companies = ['PAKRI','PPL','GTECH','OGDC','HUBC','EPCL','EFERT']

for i in companies:
    print(i)

    page = requests.get("https://dps.psx.com.pk/company/" + i)
    soup = BeautifulSoup(page.content, 'html.parser')

    share_price = soup.find_all('div', class_='stats_item')[0:3]
    current_price = soup.find_all('div', class_='quote__close')
    share_name = soup.find_all('div', class_='quote__name')


    for value2 in share_name:
        print(value2.text)

    for value in share_price:
            print(value.text)

    for value1 in current_price:
            print(value1.text)

