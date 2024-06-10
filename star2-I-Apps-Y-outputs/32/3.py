
import datetime
current_time = datetime.datetime.strptime(input(), "%H:%M:%S")
explosion_time = datetime.datetime.strptime(input(), "%H:%M:%S")
delta = explosion_time - current_time
if delta.total_seconds() < 0:
    delta += datetime.timedelta(days=1)
print((current_time + delta).strftime("%H:%M:%S"))

