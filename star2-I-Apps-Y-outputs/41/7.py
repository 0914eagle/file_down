
import datetime
date_str = input()
date_obj = datetime.datetime.strptime(date_str, "%b %d")
if date_obj.month == 10 and date_obj.day == 31 or date_obj.month == 12 and date_obj.day == 25:
    print("yup")
else:
    print("nope")

