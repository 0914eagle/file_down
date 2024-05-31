
def check_enough_coins(K, X):
    total_amount = K * 500
    if total_amount >= X:
        print("Yes")
    else:
        print("No")

# Read input from Standard Input
K, X = map(int, input().split())

# Call the function with input values
check_enough_coins(K, X)
