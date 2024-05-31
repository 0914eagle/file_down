
def calculate_happiness_points(X):
    num_500 = X // 500
    num_5 = (X % 500) // 5

    happiness_points = num_500 * 1000 + num_5 * 5
    return happiness_points

X = int(input())
print(calculate_happiness_points(X))
