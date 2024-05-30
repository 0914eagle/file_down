
import heapq

def max_longevity(n, p, c, pills):
    events = []
    for t, x, y in pills:
        events.append((t, x, y, 'start'))
        events.append((t + x, x, y, 'end'))

    events.sort()
    max_age = 0
    age = 0
    taken_pills = []
    prev_t = 0

    for t, x, y, event_type in events:
        delta_t = t - prev_t
        age += delta_t
        if event_type == 'start':
            heapq.heappush(taken_pills, (x, y))
        else:
            while taken_pills and taken_pills[0][0] != x:
                heapq.heappop(taken_pills)
            if taken_pills:
                max_age = max(max_age, age - c)
            else:
                max_age = max(max_age, age)
        prev_t = t

    return min(n, max_age)

n, p, c = map(int, input().split())
pills = [list(map(int, input().split())) for _ in range(p)]

result = max_longevity(n, p, c, pills)
print("{:.6f}".format(result))
```
