
def count_days_with_free_food(N, events):
    days = set()
    for event in events:
        for day in range(event[0], event[1] + 1):
            days.add(day)
    return len(days)

# Input parsing
N = int(input())
events = []
for _ in range(N):
    s, t = map(int, input().split())
    events.append((s, t))

# Call the function and output the result
result = count_days_with_free_food(N, events)
print(result)
