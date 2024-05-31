
def max_happiness_points(X):
    # Calculate the number of each coin type
    num_500_yen_coins = X // 500
    remaining = X % 500
    num_5_yen_coins = remaining // 5
    
    # Calculate total happiness points
    total_points = num_500_yen_coins * 1000 + num_5_yen_coins * 5
    
    return total_points

# Input
X = int(input())
print(max_happiness_points(X))
