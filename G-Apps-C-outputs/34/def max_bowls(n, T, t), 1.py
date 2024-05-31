
def max_bowls(n, T, t):
    eaten_bowls = 0
    time_elapsed = 0
    for i in range(n):
        if time_elapsed + t[i] <= T:
            eaten_bowls += 1
            time_elapsed += t[i]
        else:
            break
    return eaten_bowls

# Input parsing
n, T = map(int, input().split())
t = list(map(int, input().split()))

# Call the function and output the result
print(max_bowls(n, T, t))
