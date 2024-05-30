
def min_explosions(N, A, B, healths):
    def check(x):
        count = 0
        for h in healths:
            h -= B*x
            if h > 0:
                count += (h + A - B - 1) // (A - B)
        return count

    left, right = 0, max(healths) // A + 1
    while right - left > 1:
        mid = (left + right) // 2
        if check(mid) <= mid:
            right = mid
        else:
            left = mid
    return right

# Sample Input
N, A, B = map(int, input().split())
healths = [int(input()) for _ in range(N)]

# Output
print(min_explosions(N, A, B, healths))
```
