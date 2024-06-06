
time = input().split(":")
hour = int(time[0])
minute = int(time[1])

setHour = int(input().split(":")[0])
setMinute = int(input().split(":")[1])

time.clear()
time.append(hour)
time.append(minute)

while hour != setHour or minute != setMinute:
    if hour > setHour:
        hour -= 1
        time.insert(0, str(hour))
    elif hour < setHour:
        hour += 1
        time.insert(0, str(hour))
    if minute > setMinute:
        minute -= 1
        time.append(str(minute))
    elif minute < setMinute:
        minute += 1
        time.append(str(minute))
    print(":".join(time))
