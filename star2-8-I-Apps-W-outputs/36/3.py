
n, k = map(int, input().split())
price = list(map(int, input().split()))
max_profit = 0
for i in range(n-1):
    for j in range(i+1, n):
        profit = price[j] * 100 - price[i] * 100 - k * (j - i)
        if profit > max_profit:
            max_profit = profit

print(max_profit)

