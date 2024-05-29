
def check_rectangles(q, queries):
    results = []
    
    for _ in range(q):
        n = queries[_][0]
        sides = queries[_][1]
        
        sides.sort()
        area = sides[0] * sides[-1]
        
        possible = "YES"
        for i in range(n):
            if sides[i] * sides[-(i+1)] != area:
                possible = "NO"
                break
                
        results.append(possible)
    
    return results

# Input
q = 5
queries = [
    (1, [1, 1, 10, 10]),
    (2, [10, 5, 2, 10, 1, 1, 2, 5]),
    (2, [10, 5, 1, 10, 5, 1, 1, 1]),
    (2, [1, 1, 1, 1, 1, 1, 1, 1]),
    (1, [10000, 10000, 10000, 10000])
]

# Output
print(check_rectangles(q, queries))
```
