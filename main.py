from date_management import get_date
from graph_management import graph_config

user_words = int(input('How much words have you read today? '))
graph_config(get_date(), user_words)
