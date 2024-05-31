
def count_free_food_days(N, events):
    days_count = [0] * 366
    
    for event in events:
        start_day, end_day = event
        for i in range(start_day, end_day + 1):
            days_count[i] = 1
    
    return sum(days_count)

# Parse input
N = int(input())
events = []
for _ in range(N):
    start, end = map(int, input().split())
    events.append((start, end))

# Calculate and output result
result = count_free_food_days(N, events)
print(result)
