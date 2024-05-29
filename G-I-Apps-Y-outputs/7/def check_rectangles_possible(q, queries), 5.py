
def check_rectangles_possible(q, queries):
    results = []
    
    for query in queries:
        n = query[0]
        sticks = query[1]
        
        # Sort sticks
        sticks.sort()
        
        areas = []
        
        for i in range(0, 2*n, 2):
            if sticks[i] != sticks[i+1]:   # Opposite sides should have equal length
                results.append("NO")
                break
            area = sticks[i] * sticks[4*n - i - 1]
            areas.append(area)
            
        if len(set(areas)) == 1:
            results.append("YES")
        else:
            results.append("NO")
    
    return results

# Input
q = 5
queries = [(1, [1, 1, 10, 10]), (2, [10, 5, 2, 10, 1, 1, 2, 5]), (2, [10, 5, 1, 10, 5, 1, 1, 1]), (2, [1, 1, 1, 1, 1, 1, 1, 1]), (1, [10000, 10000, 10000, 10000])]

# Output
print(check_rectangles_possible(q, queries))
```
