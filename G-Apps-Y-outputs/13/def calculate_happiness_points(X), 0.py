
def calculate_happiness_points(X):
    happiness_points = 0

    # Calculate the number of 500-yen coins
    num_500_yen_coins = X // 500
    happiness_points += num_500_yen_coins * 1000

    # Calculate the remaining amount after exchanging for 500-yen coins
    remaining_amount = X % 500

    # Calculate the number of 5-yen coins
    num_5_yen_coins = remaining_amount // 5
    happiness_points += num_5_yen_coins * 5

    return happiness_points

X = int(input())
print(calculate_happiness_points(X))
