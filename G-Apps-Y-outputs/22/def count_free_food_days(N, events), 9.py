
def count_free_food_days(N, events):
    days = set()
    for event in events:
        for i in range(event[0], event[1] + 1):
            days.add(i)
    return len(days)

# Input
N = int(input())
events = []
for _ in range(N):
    s, t = map(int, input().split())
    events.append((s, t))

# Output
print(count_free_food_days(N, events))
