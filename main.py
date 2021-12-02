import requests
import os

from urllib.parse import urlparse

from dotenv import load_dotenv
load_dotenv()


def is_bitlink(short_input, headers):
    
    response = requests.get('https://api-ssl.bitly.com/v4/bitlinks/{}'.format(short_input), headers=headers)

    return response.ok
    
def count_clicks(short_input, headers): 
    
    params = (
        ('unit', 'day'),
        ('units', '-1'),
        ('unit_reference', '2021-11-20T12:09:11+0000'),
    )   

    response = requests.get('https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'.format(short_input), headers=headers, params=params)
    response.raise_for_status()
    clicks_count = response.json()['total_clicks']

    return clicks_count

def shorten_link(user_input, headers):

    data = {'long_url': user_input, 'domain': 'bit.ly', 'group_guid': 'Blb54sihppy'}
    response = requests.post('https://api-ssl.bitly.com/v4/bitlinks', headers=headers, json=data) 
    response.raise_for_status()
    bitlink = response.json()['link']
    return bitlink

def main():
    token = os.environ['BITLY_API_TOKEN']
    headers = {
            'Authorization': 'Bearer {}'.format(token),
            'Content-Type': 'application/json',
        }

    user_input = input('Введите ссылку: ')
    short_input = urlparse(user_input)._replace(scheme='').geturl()


    try:
        if is_bitlink(short_input, headers):
            print('Всего переходов', count_clicks(short_input, headers),'раз(а)')
        else:
            print('Битлинк', shorten_link(user_input, headers))
    except requests.exceptions.HTTPError as error:
        exit('Не могу загрузить данные из сервера:\n{0}'.format(error)) 
   
if __name__ == "__main__":
    main()
