from date_management import get_date
from graph_management import graph_config
from ui import AppInterface

userInterface = AppInterface()
userInterface.date_label.config(text='asdasdadasdsa')

# user_words = int(input('How much words have you read today? '))
graph_config(get_date(), 1)


