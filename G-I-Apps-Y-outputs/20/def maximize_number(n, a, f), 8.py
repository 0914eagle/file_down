
def maximize_number(n, a, f):
    max_num = list(map(int, a))
    
    for i in range(n):
        original_digit = int(a[i])
        modified_digit = f[original_digit - 1]
        
        if modified_digit > original_digit:
            max_num[i] = modified_digit
            break
          
    return "".join(map(str, max_num))

# Input
n = int(input())
a = input().strip()
f = list(map(int, input().split()))

# Output
print(maximize_number(n, a, f))
```
