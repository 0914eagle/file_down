
# https://open.kattis.com/problems/petr

start = input()
finish = input()

start_split = start.split(':')
start_hour = int(start_split[0])
start_min = int(start_split[1])

finish_split = finish.split(':')
finish_hour = int(finish_split[0])
finish_min = int(finish_split[1])

time = 0
hour = start_hour
min = start_min

if start == finish:
    time = 1
    print(time)
    print(start)
else:
    time = 0
    print(time)

while finish != start:
    if hour != 0:
        hour -= 1
        time += 1
        print(str(hour).zfill(2) + ":" + str(min).zfill(2))
    elif min != 0:
        hour = 23
        min -= 1
        time += 1
        print(str(hour).zfill(2) + ":" + str(min).zfill(2))
    elif hour == 0 and min == 0:
        hour = 23
        min = 59
        time += 1
        print(str(hour).zfill(2) + ":" + str(min).zfill(2))
        
print(finish)
print(time)
