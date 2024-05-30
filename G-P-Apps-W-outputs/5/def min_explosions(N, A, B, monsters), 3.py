
def min_explosions(N, A, B, monsters):
    def check(x):
        num_explosions = 0
        for h in monsters:
            h -= x * B
            if h > 0:
                num_explosions += (h + A - B - 1) // (A - B)
        return num_explosions <= x

    l, r = 0, max(monsters) // B + 1
    while l < r:
        mid = (l + r) // 2
        if check(mid):
            r = mid
        else:
            l = mid + 1
    return l

# Input processing
input_data = input().split()
N = int(input_data[0])
A = int(input_data[1])
B = int(input_data[2])
monsters = [int(input()) for _ in range(N)]

# Call the function with input values
result = min_explosions(N, A, B, monsters)
print(result)
```
