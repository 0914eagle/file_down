
import datetime

def is_halloween(date_str):
    try:
        month, day = date_str.split()
        month_num = datetime.datetime.strptime(month, '%b').month
        date = datetime.date(2023, month_num, int(day))
        if date == datetime.date(2023, 10, 31) or date == datetime.date(2023, 12, 25):
            return "yup"
        else:
            return "nope"
    except ValueError:
        return "nope"

