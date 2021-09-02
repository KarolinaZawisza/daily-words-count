import requests
import datetime as dt
import os
from dotenv import load_dotenv

today_words: int

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

dates = ['20210901']

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
    global today_words
    today_words = quantity

    post_endpoint = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{ID}'
    post_params = {
        'date': date,
        'quantity': str(today_words),
    }

    response = requests.post(url=post_endpoint, json=post_params, headers=headers)
    print(response.text)
    print(f'First post: added {today_words} words at {date}')

def graph_update(date: str, quantity: int):
    global today_words
    today_words += quantity

    update_endpoint = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{ID}/{date}'
    update_params = {
        'quantity': str(today_words)
    }

    response = requests.put(url=update_endpoint, json=update_params, headers=headers)
    print(response.text)
    print(f'Update: added {today_words} words at {date}')

def graph_delete(date: str):
    delete_endpoint = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{ID}/{date}'

    response = requests.delete(url=delete_endpoint, headers=headers)
    print(response.text)

    global today_words
    today_words = 0

def graph_config(date: str, quantity: int):
    if date != dates[len(dates) - 1]:
        dates.append(date)
        print(dates)
        graph_post(date, quantity)
    elif date == dates[len(dates) - 1]:
        graph_update(date, quantity)


user_words = int(input('How much words have you read today? '))
graph_config(today, user_words)
