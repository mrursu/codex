import requests
import json
import sqlite3

# hello
def insert_db(offer):
    with sqlite3 .connect('ikea.db') as connection:
        cursor = connection.cursor()
        # cursor.execute("""
        #     CREATE TABLE offer(
        #         id INTEGER PRIMARY KEY AUTOINCREMENT,
        #         category TEXT,
        #         sku TEXT,
        #         price INTEGER,
        #         name TEXT, 
        #         url TEXT
        #     )
        
        # """)

        cursor.execute("""
            INSERT INTO offer
            VALUES (NULL, :category, :sku, :price, :name, :url)
        
        """, offer)

        connection.commit()




def get_product(result):
    items = result['moreProducts']['productWindow']
    for item in items:

        offer = {
            'category' : 'Кровати',
            'sku' : item['itemNo'],
            'price' : item['priceNumeral'],
            'name' : item['mainImageAlt'],
            'url' : item['pipUrl']
        }
        insert_db(offer)


def get_products():
    start = 0 
    while  True:
        params = {
            'category': '16284',
            'start': start,
            'end': start + 24,
            'sort': 'RELEVANCE',
            'store': '002',
        }
        url = 'https://sik.search.blue.cdtapps.com/ua/uk/product-list-page/more-products'
        response = requests.get(url=url, params=params)
        result = response.json()
        if len(result['moreProducts']['productWindow']) == 0:
            break

        get_product(result)
        
        start += 24
        # break


def main():
    get_products()


if __name__ == '__main__':
    main()
