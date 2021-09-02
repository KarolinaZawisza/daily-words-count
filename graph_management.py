import requests
import os
from dotenv import load_dotenv
from data_file_management import get_last_date, add_record, update_record, get_last_words

load_dotenv('C:/Users/zawis/Documents/EV/.env')

ID = os.getenv('pixela_reading_graph_id')
TOKEN = os.getenv('pixela_token')
USERNAME = os.getenv('pixela_username')
PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
graph_endpoint = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs'

headers = {
    'X-USER-TOKEN': TOKEN
}

def create_user():
    user_params = {
        'token': TOKEN,
        'username': USERNAME,
        'agreeTermsOfService': 'yes',
        'notMinor': 'yes'
    }

    requests.post(url=PIXELA_ENDPOINT, json=user_params)


def create_graph():
    graph_params = {
        'id': ID,
        'name': 'reading-tracker',
        'unit': 'words',
        'type': 'int',
        'color': 'ajisai'
    }

    requests.post(url=graph_endpoint, json=graph_params, headers=headers)

def graph_post(date: str, quantity: int):
    add_record(date, quantity)
    post_endpoint = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{ID}'
    post_params = {
        'date': date,
        'quantity': str(quantity),
    }

    response = requests.post(url=post_endpoint, json=post_params, headers=headers)
    print(response.text)
    print(f'[GM-Post] Added {quantity} words at {date}')

def graph_update(date: str, quantity: int):
    today_words = get_last_words()
    today_words += quantity
    update_record(today_words)
    update_endpoint = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{ID}/{date}'
    update_params = {
        'quantity': str(today_words)
    }

    response = requests.put(url=update_endpoint, json=update_params, headers=headers)
    print(response.text)
    print(f'[GM-Update] Added {today_words} words at {date}')

def graph_delete(date: str):
    delete_endpoint = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{ID}/{date}'

    response = requests.delete(url=delete_endpoint, headers=headers)
    print(response.text)

def graph_config(date: str, quantity: int):
    if date != str(get_last_date()):
        print('!=', date, str(get_last_date()))
        graph_post(date, quantity)
    elif date == str(get_last_date()):
        print('==')
        graph_update(date, quantity)
