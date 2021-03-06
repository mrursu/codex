from turtle import heading
import beautiful
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import csv
import json 


def get_data():
    ua = UserAgent()


    headers = {
        'Accept': '*/*',
        'User-Agent': ua.random
    }

    response = requests.get(url ='https://be.tommy.com/heren-t-shirts?scrollPage=4',headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    pagination = int(soup.find('span','pagination__page--total_2vGbA').text)



    # print(type(pagination))

    with open('catalog_list.csv','w') as file:
        writer = csv.writer(file)

        writer.writerow(
            (
                'Названия товара',
                'Старая цена',
                'Новая цена',
                'Ссылка'
            )
        )

    new_dict = {}

    for item in range(1, 2 ):
        url = f'https://be.tommy.com/heren-t-shirts?scrollPage={item}'
        response = requests.get(url = url, headers = headers)

        soup = BeautifulSoup(response.text, 'lxml')

        name = soup.find_all('div','product-tile__details_1qcX9')
        
        for items in name:
            name = items.find('h4', class_ = 'product-tile__header_3k1G8').text
            try:
                 old_price = items.find('span',class_ = 'price-display__was_74nqI').text
            except:
                old_price = 'not old price'

            new_price = items.find('span',class_ = 'price-display__selling_Ub68r').text

            href_product = 'https://be.tommy.com/' + items.find('a', class_ = 'product-tile__anchor_1ujO3').get('href')

            with open('catalog_list.csv','a') as file:
                writer = csv.writer(file)

                writer.writerow(
                    (
                        name,
                        old_price,
                        new_price,
                        href_product
                        
                    )
                )

                new_dict[item] = {
                    'title': name,
                    'href': href_product
                }
            
            with open('new_dict.json', 'w') as file:
                json.dump(new_dict,file,indent=4, ensure_ascii=False)



    print('[INFO] Файл успешно записан....')
            
            # print(price)
         





        
        # response = requests.get(url =f f'https://be.tommy.com/heren-t-shirts?scrollPage={item}')
        # soup = BeautifulSoup(response.text, 'lxml')

        # for x in soup:
        #     name = x.find('h4','product-tile__header_3k1G8').text

        
            
        



def main():
    get_data()


if __name__ == '__main__':
    main()
