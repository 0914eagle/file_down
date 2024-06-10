
n = int(input())
a = list(map(int, input().split()))

def is_valid_day(events):
    stack = []
    for e in events:
        if e > 0:
            if e in stack:
                return False
            stack.append(e)
        else:
            if -e not in stack:
                return False
            stack.remove(-e)
    return len(stack) == 0

def solve(events):
    days = []
    for i in range(len(events)):
        day = [events[i]]
        i += 1
        while i < len(events) and is_valid_day(day + [events[i]]):
            day.append(events[i])
            i += 1
        days.append(day)
    return days

days = solve(a)
if len(days) == 0:
    print(-1)
else:
    print(len(days))
    print(' '.join(map(str, [len(d) for d in days])))

