
def count_shichi_go_san_numbers(N):
    count = 0
    for i in range(1, N+1):
        if set(str(i)) >= set(['7', '5', '3']):
            count += 1
    return count

# Sample Input
N = 575
print(count_shichi_go_san_numbers(N))
```
