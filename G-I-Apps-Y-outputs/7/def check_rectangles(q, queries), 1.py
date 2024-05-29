
def check_rectangles(q, queries):
    for query in queries:
        n = query[0]
        sticks = query[1]

        sticks.sort()

        area = sticks[0] * sticks[-1]
        for i in range(n):
            if sticks[i] * sticks[-(i+1)] != area or sticks[i*2] != sticks[i*2+1] or sticks[-(i*2+1)] != sticks[-(i*2+2)]:
                print("NO")
                break
        else:
            print("YES")

q = 5
queries = [
    (1, [1, 1, 10, 10]),
    (2, [10, 5, 2, 10, 1, 1, 2, 5]),
    (2, [10, 5, 1, 10, 5, 1, 1, 1]),
    (2, [1, 1, 1, 1, 1, 1, 1, 1]),
    (1, [10000, 10000, 10000, 10000])
]

check_rectangles(q, queries)
```
