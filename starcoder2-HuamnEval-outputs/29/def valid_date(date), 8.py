
def valid_date(date):
    try:
        datetime.datetime.strptime(date, '%m-%d-%Y')
        return True
    except:
        return False
