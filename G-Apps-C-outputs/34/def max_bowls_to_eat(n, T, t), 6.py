
def max_bowls_to_eat(n, T, t):
    t.sort()
    bowls_eaten = 0
    time_elapsed = 0
    for i in range(n):
        time_to_bowl = t[i]
        if time_elapsed + time_to_bowl <= T:
            bowls_eaten += 1
            time_elapsed += time_to_bowl
        else:
            break
    return bowls_eaten

# Input
n, T = map(int, input().split())
t = list(map(int, input().split()))

# Output
print(max_bowls_to_eat(n, T, t))
