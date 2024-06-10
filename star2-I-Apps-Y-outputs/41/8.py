
import datetime

def is_halloween(date_str):
    date_format = '%b %d'
    date = datetime.datetime.strptime(date_str, date_format)
    if date.month == 10 and date.day == 31:
        return True
    elif date.month == 12 and date.day == 25:
        return True
    else:
        return False

def print_halloween_status(date_str):
    if is_halloween(date_str):
        print('yup')
    else:
        print('nope')

date_str = input()
print_halloween_status(date_str)

