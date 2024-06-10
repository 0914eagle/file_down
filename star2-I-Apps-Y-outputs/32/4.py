
import datetime

current_time = datetime.datetime.strptime(input(), "%H:%M:%S")
explosion_time = datetime.datetime.strptime(input(), "%H:%M:%S")

time_to_explosion = explosion_time - current_time

print(time_to_explosion.strftime("%H:%M:%S"))

