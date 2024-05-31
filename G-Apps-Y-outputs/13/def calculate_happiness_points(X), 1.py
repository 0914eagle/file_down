
def calculate_happiness_points(X):
    num_500_yen = X // 500
    remaining = X % 500

    num_5_yen = remaining // 5

    happiness_points = num_500_yen * 1000 + num_5_yen * 5
    return happiness_points

X = int(input())
print(calculate_happiness_points(X))
