
def calculate_max_happiness_points(X):
    # Calculate the maximum number of 500-yen coins Takahashi can exchange for
    num_500_yen_coins = X // 500

    # Calculate the remaining amount after exchanging 500-yen coins
    remaining_amount = X % 500

    # Calculate the number of 5-yen coins that can be obtained from the remaining amount
    num_5_yen_coins = remaining_amount // 5

    # Calculate the total happiness points earned
    total_happiness_points = num_500_yen_coins * 1000 + num_5_yen_coins * 5

    return total_happiness_points

# Read input from Standard Input
X = int(input())

# Print the maximum number of happiness points that can be earned
print(calculate_max_happiness_points(X))
