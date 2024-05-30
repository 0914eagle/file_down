
def count_shichi_go_san_numbers(N):
    count = 0
    for i in range(1, N+1):
        if all(digit in str(i) for digit in ['7', '5', '3']):
            count += 1
    return count

N = int(input())
result = count_shichi_go_san_numbers(N)
print(result)
```
