
def minimum_amount(N, K, digits_disliked):
    while True:
        flag = False
        for digit in str(N):
            if int(digit) in digits_disliked:
                flag = True
                break
        if not flag:
            return N
        N += 1

# Reading input
N, K = map(int, input().split())
digits_disliked = list(map(int, input().split()))

result = minimum_amount(N, K, digits_disliked)
print(result)
```
