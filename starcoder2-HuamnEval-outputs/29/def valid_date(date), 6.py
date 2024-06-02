
def valid_date(date):
    if date == '':
        return False
    else:
        date_list = date.split('-')
        if len(date_list) != 3:
            return False
        else:
            month = int(date_list[0])
            day = int(date_list[1])
            year = int(date_list[2])
            if month < 1 or month > 12:
                return False
            if day < 1 or day > 31:
                return False
            if month == 2:
                if day < 1 or day > 29:
                    return False
            if month == 4 or month == 6 or month == 9 or month == 11:
                if day < 1 or day > 30:
                    return False
            return True
 