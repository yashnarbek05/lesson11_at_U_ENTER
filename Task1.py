from datetime import datetime


def days_until_new_year():
    today = datetime.now()
    new_year = datetime(today.year + 1, 1, 1)
    delta = new_year - today
    return delta

if __name__ == '__main__':
    print(days_until_new_year())