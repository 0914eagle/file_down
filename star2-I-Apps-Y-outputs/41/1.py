
import datetime

def is_halloween(date_str):
    date = datetime.datetime.strptime(date_str, "%b %d")
    if date.month == 10 and date.day == 31:
        return "yup"
    elif date.month == 12 and date.day == 25:
        return "yup"
    else:
        return "nope"

date_str = input()
print(is_halloween(date_str))

