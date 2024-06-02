
def find_same_temperature(X, Y):
    if Y == 1:
        if X == 0:
            return "ALL GOOD"
        else:
            return "IMPOSSIBLE"
    else:
        temp = -X / (Y - 1)
        if temp.is_integer():
            return int(temp)
        else:
            return "IMPOSSIBLE"

# Input
X, Y = map(int, input().split())

# Output
result = find_same_temperature(X, Y)
print(result)
