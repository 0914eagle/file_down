
n, k = map(int, input().split())
prices = list(map(int, input().split()))
min_price = 100001
max_profit = 0
for i in range(n):
    min_price = min(min_price, prices[i])
    max_profit = max(max_profit, prices[i] - min_price - i * k)
print(max_profit)

