
def max_bowls_to_eat(n, T, t):
    bowls_eaten = 0
    time_elapsed = 0
    for i in range(n):
        if time_elapsed + 1 <= t[i] and time_elapsed + 1 <= T:
            bowls_eaten += 1
            time_elapsed += 1
        elif time_elapsed < t[i] and time_elapsed + 1 > T:
            break
        else:
            time_elapsed += 1
    return bowls_eaten

# Input parsing
n, T = map(int, input().split())
t = list(map(int, input().split()))

result = max_bowls_to_eat(n, T, t)
print(result)
