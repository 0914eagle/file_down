
import datetime

def time_diff(time1, time2):
    time1 = datetime.datetime.strptime(time1, "%H:%M:%S")
    time2 = datetime.datetime.strptime(time2, "%H:%M:%S")
    return (time2 - time1).total_seconds()

current_time = input()
explosion_time = input()

time_to_explosion = time_diff(current_time, explosion_time)
time_to_explosion %= 24 * 3600

explosion_time = datetime.datetime.strptime(current_time, "%H:%M:%S") + datetime.timedelta(seconds=time_to_explosion)
explosion_time = explosion_time.strftime("%H:%M:%S")

print(explosion_time)

