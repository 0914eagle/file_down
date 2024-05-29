
def check_rectangles_area(q, queries):
    results = []
    for query in queries:
        n = query[0]
        sides = sorted(query[1], reverse=True)
        target_area = sides[0] * sides[-1]

        possible_rectangles = {}
        while sides:
            side1 = sides.pop(0)
            side2 = sides.pop()
            current_area = side1 * side2
            if current_area != target_area:
                results.append("NO")
                break
            possible_rectangles[current_area] = possible_rectangles.get(current_area, 0) + 1

        if len(possible_rectangles) == n:
            results.append("YES")
        elif len(possible_rectangles) < n:
            results.append("NO")

    return results

q = 5
queries = [
    (1, [1, 1, 10, 10]),
    (2, [10, 5, 2, 10, 1, 1, 2, 5]),
    (2, [10, 5, 1, 10, 5, 1, 1, 1]),
    (2, [1, 1, 1, 1, 1, 1, 1, 1]),
    (1, [10000, 10000, 10000, 10000])
]

results = check_rectangles_area(q, queries)
for result in results:
    print(result)
```
