
def max_bowls_to_eat(n, T, bowls_time):
    bowls_eaten = 0
    current_time = 0
    for time in bowls_time:
        if current_time + time <= T:
            bowls_eaten += 1
            current_time += time
        else:
            break
    return bowls_eaten

# Input parsing
n, T = map(int, input().split())
bowls_time = list(map(int, input().split()))

# Call the function
result = max_bowls_to_eat(n, T, bowls_time)
print(result)
