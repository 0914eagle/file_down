
def count_shichi_go_san_numbers(N):
    count = 0
    for i in range(1, N+1):
        if all(d in str(i) for d in ['7', '5', '3']):
            count += 1
    return count

N = int(input())
print(count_shichi_go_san_numbers(N))
```
