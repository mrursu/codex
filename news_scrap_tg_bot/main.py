from operator import imod
from urllib import response
from wsgiref import headers
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from datetime import datetime
import time


def get_first_news():

    ua = UserAgent()
    headers = {
        'User-Agent': ua.random
    }

    url = 'https://www.securitylab.ru/news/'
    response = requests.get(url = url, headers = headers)
    soup = BeautifulSoup(response.text, 'lxml')
    



def main():
    pass

if __name__ == '__main__':
    main()