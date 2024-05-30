
def is_shichi_go_san(num):
    num_str = str(num)
    return '7' in num_str and '5' in num_str and '3' in num_str

def count_shichi_go_san_numbers(N):
    count = 0
    for i in range(1, N+1):
        if is_shichi_go_san(i):
            count += 1
    return count

N = int(input())
print(count_shichi_go_san_numbers(N))
```
