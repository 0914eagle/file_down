
def check_coins(K, X):
    total_amount = K * 500
    if total_amount >= X:
        print("Yes")
    else:
        print("No")

# Read input from Standard Input
K, X = map(int, input().split())

# Check if the coins add up to X yen or more
check_coins(K, X)
