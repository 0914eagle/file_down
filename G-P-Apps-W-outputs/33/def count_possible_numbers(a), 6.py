
def count_possible_numbers(a):
    count = 0
    a = list(map(int, a))
    
    while True:
        found = False
        for i in range(len(a) - 1):
            if a[i] + a[i+1] == 9:
                a[i] = 9
                a.pop(i+1)
                found = True
                break
        
        if not found:
            break
    
    if a.count(9) == len(a):
        count = 1
    else:
        count = (a.count(9) + 1) // 2
        
    return count

# Read input
a = input().strip()

# Call the function and print the output
print(count_possible_numbers(a))
```
