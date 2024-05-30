
def count_shichi_go_san_numbers(N):
    count = 0
    for i in range(1, N+1):
        if set(str(i)) == {'3', '5', '7'}:
            count += 1
    return count

N = int(input())
result = count_shichi_go_san_numbers(N)
print(result)
```
