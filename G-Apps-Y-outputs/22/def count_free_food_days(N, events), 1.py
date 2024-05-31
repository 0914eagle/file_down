
def count_free_food_days(N, events):
    days = set()
    for event in events:
        for day in range(event[0], event[1] + 1):
            days.add(day)
    return len(days)

# Reading input
N = int(input())
events = []
for _ in range(N):
    s, t = map(int, input().split())
    events.append((s, t))

# Calling the function and printing the output
print(count_free_food_days(N, events))
