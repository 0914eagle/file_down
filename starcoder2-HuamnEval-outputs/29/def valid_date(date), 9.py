
def valid_date(date):
    try:
        date = datetime.strptime(date, '%m-%d-%Y')
        return True
    except ValueError:
        return False
 