
def exponial(n, m):
    def exponial_helper(n, m):
        if n == 1:
            return 1
        return pow(n, exponial_helper(n-1, m), m)
    
    return exponial_helper(n, m)

n, m = map(int, input().split())
result = exponial(n, m)
print(result)
```
