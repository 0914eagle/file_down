
def is_shichi_go_san(num):
    contains_7 = False
    contains_5 = False
    contains_3 = False
    for digit in str(num):
        if digit == '7':
            contains_7 = True
        elif digit == '5':
            contains_5 = True
        elif digit == '3':
            contains_3 = True
        else:
            return False
    return contains_7 and contains_5 and contains_3

def count_shichi_go_san_numbers(N):
    count = 0
    for i in range(1, N+1):
        if is_shichi_go_san(i):
            count += 1
    return count

N = int(input())
print(count_shichi_go_san_numbers(N))
```
