
def hand_money(N, K, disliked_digits):
    def is_disliked(num):
        num_str = str(num)
        for d in disliked_digits:
            if str(d) in num_str:
                return True
        return False

    while is_disliked(N):
        N += 1
    return N

N, K = map(int, input().split())
disliked_digits = list(map(int, input().split()))

result = hand_money(N, K, disliked_digits)
print(result)
```
