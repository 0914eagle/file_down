
def calculate_happiness_points(X):
    # Calculate the number of 500-yen coins and remaining amount after exchanging those coins
    num_500_yen_coins = X // 500
    remaining_amount = X - num_500_yen_coins * 500

    # Calculate the number of 5-yen coins from the remaining amount
    num_5_yen_coins = remaining_amount // 5

    # Calculate total happiness points
    total_happiness_points = num_500_yen_coins * 1000 + num_5_yen_coins * 5

    return total_happiness_points

X = int(input())
happiness_points = calculate_happiness_points(X)
print(happiness_points)
