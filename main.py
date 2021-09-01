import requests
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv('C:/Users/zawis/Documents/EV/.env')

today = dt.datetime.now().strftime('%Y%m%d')

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

def graph_post(date: str, quantity: str):
    post_endpoint = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{ID}'
    post_params = {
        'date': date,
        'quantity': quantity,
    }

    response = requests.post(url=post_endpoint, json=post_params, headers=headers)
    print(response.text)

def graph_update(date, quantity):
    update_endpoint = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{ID}/{date}'
    update_params = {
        'quantity': quantity
    }

    response = requests.put(url=update_endpoint, json=update_params, headers=headers)
    print(response.text)

def graph_delete(date):
    delete_endpoint = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{ID}/{date}'

    response = requests.delete(url=delete_endpoint, headers=headers)
    print(response.text)


user_words = input('How much words have you read today? ')

graph_update(today, user_words)
