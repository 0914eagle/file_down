
def total_shares_on_trading_days():
    C = int(input())  # Total number of companies
    shares_dict = {}

    for _ in range(C):
        K = int(input())  # Number of records for this company
        for _ in range(K):
            N, D = map(int, input().split())
            if D not in shares_dict:
                shares_dict[D] = 0
            shares_dict[D] += N

    trading_days = sorted(shares_dict.keys())
    for day in trading_days:
        print(shares_dict[day], end=" ")

total_shares_on_trading_days()
```
