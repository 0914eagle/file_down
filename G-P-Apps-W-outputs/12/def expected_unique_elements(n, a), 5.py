
def expected_unique_elements(n, a):
    total_sum = sum(set(a))
    return total_sum * 2 - total_sum / n

n = int(input())
a = list(map(int, input().split()))

result = expected_unique_elements(n, a)
print("{:.6f}".format(result))
```
