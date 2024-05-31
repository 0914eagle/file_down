
def calculate_happiness_points(X):
    happiness_points = 0
    happiness_points += (X // 500) * 1000
    X %= 500
    happiness_points += (X // 5) * 5
    return happiness_points

X = int(input())
print(calculate_happiness_points(X))
