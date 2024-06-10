
n = int(input())
a = list(map(int, input().split()))

def is_valid_day(events):
    stack = []
    for event in events:
        if event > 0:
            if event in stack:
                return False
            stack.append(event)
        else:
            if -event not in stack:
                return False
            stack.remove(-event)
    return len(stack) == 0

def partition(events):
    days = []
    current_day = []
    for event in events:
        current_day.append(event)
        if is_valid_day(current_day):
            days.append(current_day)
            current_day = []
    if len(current_day) > 0:
        days.append(current_day)
    return days

days = partition(a)
if len(days) == 0:
    print(-1)
else:
    print(len(days))
    print(' '.join(map(str, [len(day) for day in days])))

