from unicodedata import category
import requests
import json


def get_product():
    url = 'https://xl-catalog-api.rozetka.com.ua/v4/goods/getDetails?front-type=xl&country=UA&lang=ru&with_groups=1&with_docket=1&goods_group_href=1&product_ids=55377432,262986281,32939575,275798898,176810684,20864831,6800309,1528982,287170143,268659266,268658901,11953089,9962201,21155674,7344520,317922337,317922328,287202298,43353000,317922334,78344966,263013516,275598133,263004881,14829236,177172052,264634686,263006566,43354416,268659491,264463126,118478665,176915859,331717078,264594071,61816956,264558806,231818635,331708675,231811465,43354360,5483211,331709740,43353976,251770376,310637493,287190443,335206948,312065620,302844183,315990250,302844203,266684926,312065764,302844828,317426854,325443196,35891063,302844533,321006613'
    response = requests.get(url = url)


def get_articles():
    url = 'https://xl-catalog-api.rozetka.com.ua/v4/goods/get?'
    # front-type=xl&country=UA&lang=ru&page=1&category_id=146633
    page = 1
    ids1 = {}
    while True:
        params = (
            ('front-typ', 'xl'),
            ('contry','UA'),
            ('lang', 'ru'),
            ('page', page),
            ('category_id', 146633)
        )


        response = requests.get(url = url, params = params)
        result = response.json()

        total_page = result['data']['total_pages']  
        ids = result['data']['ids']

        ids1[page] = ids
        if page  >=  total_page:
            break

    
        page += 1
    print(ids1)
        
        



def main():
    get_articles()

if __name__ == '__main__':
    main()