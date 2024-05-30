
def candy_wrappers(t, cases):
    for n in cases:
        x = 1
        while n % (2*x - 1) != 0:
            x += 1
        print(x)

# Input processing
t = int(input())
cases = [int(input()) for _ in range(t)]

# Call the function
candy_wrappers(t, cases)
```
