
def max_bowls_eaten(n, T, bowls_ready):
    bowls_eaten = 0
    time_left = T

    for t in bowls_ready:
        if t <= time_left:
            bowls_eaten += 1
            time_left -= t
        else:
            break

    return bowls_eaten

# Input
n, T = map(int, input().split())
bowls_ready = list(map(int, input().split()))

# Output
print(max_bowls_eaten(n, T, bowls_ready))
