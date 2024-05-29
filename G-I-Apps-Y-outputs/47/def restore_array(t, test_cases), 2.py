
def restore_array(t, test_cases):
    for i in range(t):
        n, x, y = test_cases[i]
        
        diff = y - x
        elements = [x]
        
        for j in range(2, n):
            if j * diff % n == 0:
                start = (x - (j-1) * diff // n) + diff
                for k in range(j):
                    elements.append(start + k * diff)
                break
        
        while len(elements) < n:
            elements.append(elements[-1] - diff)
        
        print(*elements)

# Example usage
t = 5
test_cases = [(2, 1, 49), (5, 20, 50), (6, 20, 50), (5, 3, 8), (9, 13, 22)]
restore_array(t, test_cases)
```
