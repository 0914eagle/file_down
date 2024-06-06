
def SetTime(times,initialTime,currentTime):
    if currentTime == initialTime:
        return 0
    elif currentTime in times:
        return 1
    else:
        times.add(currentTime)
        initialHour,initialMinute = map(int,initialTime.split(':'))
        initialMinute = initialMinute % 10 + 10*(initialMinute//10)
        currentHour,currentMinute = map(int,currentTime.split(':'))
        currentMinute = currentMinute % 10 + 10*(currentMinute//10)
        print(initialTime,currentTime)
        if initialMinute != currentMinute:
            currentTime = str(currentHour) + (":" if len(str(currentMinute))==2 else ":0") + str(currentMinute)
            times.add(currentTime)
            return SetTime(times,initialTime,currentTime)
        elif initialHour != currentHour:
            currentTime = str(currentHour) + (":00" if currentMinute==0 else (":0" if currentMinute//10==0 else ":" + str(currentMinute)))
            times.add(currentTime)
            return SetTime(times,initialTime,currentTime)
        else:
            return 1

if __name__ == "__main__":
    times = set()
    initialTime = input()
    currentTime = input()
    print(SetTime(times,initialTime,currentTime) + 2)
    print(initialTime)
    for time in times:
        print(time)
    print(currentTime)
