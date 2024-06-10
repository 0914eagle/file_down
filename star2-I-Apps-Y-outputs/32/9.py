
import datetime

current_time = datetime.datetime.strptime(input(), "%H:%M:%S")
explosion_time = datetime.datetime.strptime(input(), "%H:%M:%S")

time_to_explosion = explosion_time - current_time

if time_to_explosion.total_seconds() < 0:
    time_to_explosion += datetime.timedelta(days=1)

print(time_to_explosion.strftime("%H:%M:%S"))

