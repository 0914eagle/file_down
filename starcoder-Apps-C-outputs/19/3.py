
initial_time = input().split(":")
target_time = input().split(":")
hour_initial, minute_initial = int(initial_time[0]), int(initial_time[1])
hour_target, minute_target = int(target_time[0]), int(target_time[1])

hour_change = abs(hour_target - hour_initial)
minute_change = abs(minute_target - minute_initial)

if (hour_initial < 0 or hour_initial > 23 or minute_initial < 0 or minute_initial > 59 or
        hour_target < 0 or hour_target > 23 or minute_target < 0 or minute_target > 59):
    print("Invalid times")
else:
    if (hour_initial > hour_target or (hour_initial == hour_target and minute_initial > minute_target)):
        hour_change = 24 - hour_change
    print(hour_change + minute_change + 1)
    for hour in range(hour_initial, hour_initial + hour_change + 1):
        for minute in range(minute_initial, minute_initial + minute_change + 1):
            if (hour == hour_initial and minute == minute_initial):
                print(str(hour).zfill(2) + ":" + str(minute).zfill(2))
            elif (hour == hour_initial + hour_change and minute == minute_initial + minute_change):
                print(str(hour).zfill(2) + ":" + str(minute).zfill(2))
            elif (minute >= 60):
                minute = 0
                hour += 1
                print(str(hour).zfill(2) + ":" + str(minute).zfill(2))
            else:
                print(str(hour).zfill(2) + ":" + str(minute).zfill(2))

