
def count_food_days(N, events):
    food_days = set()
    
    for event in events:
        for day in range(event[0], event[1]+1):
            food_days.add(day)
    
    return len(food_days)

# Input
N = int(input())
events = []
for _ in range(N):
    s, t = map(int, input().split())
    events.append((s, t))

# Output
result = count_food_days(N, events)
print(result)
