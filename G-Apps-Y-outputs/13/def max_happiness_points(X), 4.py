
def max_happiness_points(X):
    num_500_yen_coins = X // 500
    X = X % 500
    num_5_yen_coins = X // 5
    return num_500_yen_coins * 1000 + num_5_yen_coins * 5

X = int(input())
print(max_happiness_points(X))
