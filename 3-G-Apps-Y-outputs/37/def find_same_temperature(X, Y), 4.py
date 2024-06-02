
def find_same_temperature(X, Y):
    if Y == 1:
        if X == 0:
            return 0
        else:
            return "IMPOSSIBLE"
    else:
        temp = -X / (Y - 1)
        if temp.is_integer():
            return int(temp)
        else:
            return "IMPOSSIBLE"

X, Y = map(int, input().split())
result = find_same_temperature(X, Y)
print(result)
