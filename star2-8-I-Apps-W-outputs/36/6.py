
import sys

def find_max_profit(n, k, crypto_kattis_prices):
    max_profit = 0
    
    for i in range(n):
        for j in range(i+1, n+1):
            profit = crypto_kattis_prices[j-1] - crypto_kattis_prices[i-1] - k*(j-i)
            
            if profit > max_profit:
                max_profit = profit
    
    return max_profit

n, k = map(int, input().split())
crypto_kattis_prices = list(map(int, input().split()))

max_profit = find_max_profit(n, k, crypto_kattis_prices)

print(max_profit)

