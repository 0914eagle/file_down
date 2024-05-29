
def expected_money_spent(N, P):
    res = 0.0
    for i in range(1, N+1):
        cost = 5.0
        catch_prob = P
        for _ in range(100):
            cost += catch_prob * 0.01
            catch_prob *= (1 - 0.01 * P)
            if catch_prob == 0:
                break
        res += cost
    return res

# Input
N, P = map(float, input().strip().split())

# Output
result = expected_money_spent(int(N), P)
print("{:.9f}".format(result))
```
