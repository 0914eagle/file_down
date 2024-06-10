
def solve_short_sell(n_days, daily_prices, cost_per_day):
    min_price_seen = float("inf")
    max_profit = 0
    
    for day in range(n_days):
        min_price_seen = min(min_price_seen, daily_prices[day])
        max_profit = max(max_profit, daily_prices[day] - min_price_seen - cost_per_day)
    
    return max_profit
n, k = map(int, input().split())
prices = list(map(int, input().split()))

max_profit = solve_short_sell(n, prices, k)
print(max_profit)

