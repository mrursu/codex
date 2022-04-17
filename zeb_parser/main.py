import beautiful
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


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

    for item in range(1, pagination + 1):
        response = requests.get(url = f'https://be.tommy.com/heren-t-shirts?scrollPage={item}')

        soup = BeautifulSoup(response.text, 'lxml')

        name = soup.find_all('h4','product-tile__header_3k1G8')
        for x in name:
            print(x.text)



        
        # response = requests.get(url =f f'https://be.tommy.com/heren-t-shirts?scrollPage={item}')
        # soup = BeautifulSoup(response.text, 'lxml')

        # for x in soup:
        #     name = x.find('h4','product-tile__header_3k1G8').text

        
            
        



def main():
    get_data()


if __name__ == '__main__':
    main()
