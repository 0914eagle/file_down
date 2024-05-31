
def max_bowls(n, T, t):
    eaten = 0
    current_time = 0
    for i in range(n):
        if current_time + 1 <= T:
            current_time += 1
            if current_time >= t[i]:
                eaten += 1
    return eaten

# Input
n, T = map(int, input().split())
t = list(map(int, input().split()))

# Output
print(max_bowls(n, T, t))
