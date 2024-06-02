
def find_same_temperature(X, Y):
    if Y == 1:
        if X == 0:
            return 0
        else:
            return "IMPOSSIBLE"
    else:
        temperature = -X / (Y - 1)
        if temperature.is_integer():
            return int(temperature)
        else:
            return "IMPOSSIBLE"

# Input
X, Y = map(int, input().split())

# Output
result = find_same_temperature(X, Y)
print(result)
