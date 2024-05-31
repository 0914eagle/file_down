
def max_bowls(n, T, times):
    eaten = 0
    current_time = 0
    for t in times:
        if t > T:
            break
        current_time += 1
        if current_time + t <= T:
            eaten += 1
    return eaten

# Input parsing
n, T = map(int, input().split())
times = list(map(int, input().split()))

# Call the function with input values
result = max_bowls(n, T, times)
print(result)
