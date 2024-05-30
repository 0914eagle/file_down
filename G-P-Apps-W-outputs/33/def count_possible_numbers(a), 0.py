
def count_possible_numbers(a):
    count = 0
    a = list(map(int, str(a)))
    n = len(a)
    
    for i in range(n-1):
        if a[i] + a[i+1] == 9:
            count += 1
    
    return (count + 1) // 2

# Reading input
a = input().strip()

# Output
print(count_possible_numbers(a))
```
