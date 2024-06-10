
N, K = map(int, input().split())
prices = list(map(int, input().split()))

max_profit = 0
for borrow_day in range(N):
    for repay_day in range(borrow_day + 1, N + 1):
        profit = prices[repay_day - 1] - prices[borrow_day] - K * (repay_day - borrow_day)
        if profit > max_profit:
            max_profit = profit

print(max_profit)

