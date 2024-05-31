
def max_bowls(n, T, times):
    times.sort()
    eaten_bowls = 0
    time_elapsed = 0

    for i in range(n):
        if time_elapsed + times[i] <= T:
            eaten_bowls += 1
            time_elapsed += times[i]
        else:
            break

    return eaten_bowls

# Input parsing
n, T = map(int, input().split())
times = list(map(int, input().split()))

result = max_bowls(n, T, times)
print(result)
