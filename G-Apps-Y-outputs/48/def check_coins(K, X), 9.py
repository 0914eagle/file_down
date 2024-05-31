
def check_coins(K, X):
    total = K * 500
    if total >= X:
        print("Yes")
    else:
        print("No")

# Read input from Standard Input
K, X = map(int, input().split())
check_coins(K, X)
