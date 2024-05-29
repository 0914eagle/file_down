
def can_create_rectangles_of_equal_area(n, sticks):
    sticks.sort()
    area = sticks[0] * sticks[-1]
    i, j = 0, len(sticks) - 1
    while i < j:
        if sticks[i] * sticks[j] != area or sticks[i] != sticks[i+1] or sticks[j] != sticks[j-1]:
            return "NO"
        i += 2
        j -= 2
    return "YES"

q = int(input())
for _ in range(q):
    n = int(input())
    sticks = list(map(int, input().split()))
    result = can_create_rectangles_of_equal_area(n, sticks)
    print(result)
```
