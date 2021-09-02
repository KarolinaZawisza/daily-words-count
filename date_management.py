import datetime as dt

def get_date() -> str:
    today = dt.datetime.now().strftime('%Y%m%d')

    return today
