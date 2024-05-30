
def solve_candy_wrappers(t, test_cases):
    for n in test_cases:
        x = 1
        while n % ((2 ** x) - 1) != 0:
            x += 1
        print(n // ((2 ** x) - 1))

# Input parsing
t = int(input())
test_cases = [int(input()) for _ in range(t)]

# Call the function to solve the candy wrappers problem
solve_candy_wrappers(t, test_cases)
```
