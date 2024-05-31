
def check_coins(K, X):
    total_yen = K * 500
    if total_yen >= X:
        print("Yes")
    else:
        print("No")

# Read input from Standard Input
K, X = map(int, input().split())
check_coins(K, X)
