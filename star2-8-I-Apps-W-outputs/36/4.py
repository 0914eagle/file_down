
def max_profit(N, K, prices):
  min_price = float('inf')
  max_profit = 0
  for price in prices:
    min_price = min(min_price, price)
    max_profit = max(max_profit, price - min_price - K)
  return max_profit

N, K = map(int, input().split())
prices = list(map(int, input().split()))

print(max_profit(N, K, prices))

