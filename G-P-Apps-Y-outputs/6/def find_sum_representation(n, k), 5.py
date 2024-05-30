
def find_sum_representation(n, k):
    if n < k or (n % 2 != k % 2):
        return "NO"
    
    if n % 2 == 0:
        return "YES\n" + " ".join([str(n // k)] * k)
    else:
        if k == 1:
            return "YES\n" + str(n)
        else:
            return "YES\n" + " ".join([str(n // k + 1)] * (n % k) + [str(n // k)] * (k - n % k))

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(find_sum_representation(n, k))
```
