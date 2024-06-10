
import datetime

def time_diff(time1, time2):
    time1 = datetime.datetime.strptime(time1, "%H:%M:%S")
    time2 = datetime.datetime.strptime(time2, "%H:%M:%S")
    return (time2 - time1).total_seconds()

def time_add(time, seconds):
    time = datetime.datetime.strptime(time, "%H:%M:%S")
    return (time + datetime.timedelta(seconds=seconds)).strftime("%H:%M:%S")

current_time = input()
explosion_time = input()

time_to_explosion = time_diff(current_time, explosion_time)
time_to_explosion = max(time_to_explosion, 1)
time_to_explosion = min(time_to_explosion, 24 * 60 * 60)

print(time_add(current_time, time_to_explosion))

