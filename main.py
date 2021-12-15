import argparse
import requests
import os

from urllib.parse import urlparse

from dotenv import load_dotenv


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


def shorten_link(user_input, headers, user_domain, user_group_guid):

    if user_group_guid is None:
        user_group_guid = 'Blb54sihppy'

    data = {'long_url': user_input, 'domain': user_domain, 'group_guid': user_group_guid}
    response = requests.post('https://api-ssl.bitly.com/v4/bitlinks', headers=headers, json=data)
    response.raise_for_status()
    bitlink = response.json()['link']
    return bitlink


def main():
    load_dotenv()
    token = os.environ['BITLY_API_TOKEN']
    
    headers = {
            'Authorization': 'Bearer {}'.format(token),
            'Content-Type': 'application/json',
        }

    parser = argparse.ArgumentParser(
        description='Описание что делает программа'
    )
    parser.add_argument('user_input', help='ссылка пользователя')
    parser.add_argument('-d', '--domain', default='bit.ly', help='user domain')
    parser.add_argument('-g', '--group', default=None, help='user group guid')
    args = parser.parse_args()
    user_input = args.user_input
    user_domain = args.domain
    user_group_guid = args.group

    short_input = urlparse(user_input)._replace(scheme='').geturl()

    try:
        if is_bitlink(short_input, headers):
            print('Всего переходов', count_clicks(short_input, headers), 'раз(а)')
        else:
            print('Битлинк', shorten_link(user_input, headers, user_domain, user_group_guid))
    except requests.exceptions.HTTPError as error:
        exit('Не могу загрузить данные из сервера:\n{0}'.format(error))

if __name__ == "__main__":
    main()

