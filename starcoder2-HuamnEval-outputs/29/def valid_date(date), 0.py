
def valid_date(date):
    if date == '':
        return False
    if len(date) != 10:
        return False
    if date[2] != '-' or date[5] != '-':
        return False
    if not date[0].isdigit() or not date[1].isdigit() or not date[3].isdigit() or not date[4].isdigit() or not date[6].isdigit() or not date[7].isdigit() or not date[8].isdigit() or not date[9].isdigit():
        return False
    if int(date[0:2]) < 1 or int(date[0:2]) > 12:
        return False
    if int(date[0:2]) == 1 or int(date[0:2]) == 3 or int(date[0:2]) == 5 or int(date[0:2]) == 7 or int(date[0:2]) == 8 or int(date[0:2]) == 10 or int(date[0:2]) == 12:
        if int(date[3:5]) < 1 or int(date[3:5]) > 31:
            return False
    if int(date[0:2]) == 4 or int(date[0:2]) == 6 or int(date[0:2]) == 9 or int(date[0:2]) == 11:
        if int(date[3:5]) < 1 or int(date[3:5]) > 30:
            return False
    if int(date[0:2]) == 2:
        if int(date[3:5]) < 1 or int(date[3:5]) > 29:
            return False
    return True
