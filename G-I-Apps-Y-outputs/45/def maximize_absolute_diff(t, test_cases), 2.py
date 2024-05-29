
def maximize_absolute_diff(t, test_cases):
    for n, m in test_cases:
        if n == 1:
            print(0)
        elif n == 2:
            print(min(m, 2))
        else:
            if m < n:
                print((n*(n-1))//2)
            else:
                remaining_sum = m - n
                max_val = remaining_sum // (n-1)
                remaining_sum -= max_val * (n-1)
                result = max_val * (max_val+1) * (n-remaining_sum) // 2 + max_val*(remaining_sum*(remaining_sum + 1) // 2)
                print(result)

t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    test_cases.append((n, m))

maximize_absolute_diff(t, test_cases)
```
