import pandas as pd

csv_file = pd.read_csv('words_graph_stats.csv')

def get_last_date() -> str:
    last_date = csv_file.loc[len(csv_file)-1]
    return last_date['date']

def get_last_words() -> int:
    last_date = csv_file.loc[len(csv_file) - 1]
    return int(last_date['words'])

def add_record(date: str, words: int):
    data = {
        'date': [date],
        'words': [words]
    }
    df = pd.DataFrame(data)
    df.to_csv('words_graph_stats.csv', index=False, mode='a', header=False)
    print(f'[DFM] Added {words} words at {date}')

def update_record(words: int):
    csv_file.at[len(csv_file)-1, 'words'] = words
    csv_file.to_csv('words_graph_stats.csv', index=False,)
    print(f'[DFM] Changed words amount to {words}')

def get_records(amount: int) -> list:
    recent_records = []
    for row in range(0, amount):
        last_records = {
            'date': csv_file.loc[row]['date'],
            'words': csv_file.loc[row]['words']
        }
        recent_records.append(last_records)
    return recent_records

