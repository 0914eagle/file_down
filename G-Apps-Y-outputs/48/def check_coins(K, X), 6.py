
def check_coins(K, X):
    total_yen = K * 500
    if total_yen >= X:
        print("Yes")
    else:
        print("No")

# Read input from Standard Input
K, X = map(int, input().split())

# Check if the coins add up to X yen or more
check_coins(K, X)
