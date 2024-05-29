
def find_amount(N, K, dislikes):
    while True:
        str_N = str(N)
        flag = False
        for digit in str_N:
            if int(digit) in dislikes:
                flag = True
                break
        if not flag:
            return N
        N += 1

# Input
N, K = map(int, input().split())
dislikes = list(map(int, input().split()))

# Output
result = find_amount(N, K, dislikes)
print(result)
```
