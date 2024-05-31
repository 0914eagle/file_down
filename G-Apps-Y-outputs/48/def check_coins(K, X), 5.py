
def check_coins(K, X):
    total_amount = K * 500
    if total_amount >= X:
        print("Yes")
    else:
        print("No")

# Input from Standard Input
K, X = map(int, input().split())
check_coins(K, X)
