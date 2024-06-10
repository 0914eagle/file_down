
n, k = map(int, input().split())
prices = list(map(int, input().split()))
min_price = min(prices)
max_price = max(prices)
if max_price - min_price <= k:
    print(0)
else:
    min_idx = prices.index(min_price)
    max_idx = prices.index(max_price)
    profit = 0
    for i in range(min_idx+1, max_idx):
        profit += prices[i] - k
    print(profit)

