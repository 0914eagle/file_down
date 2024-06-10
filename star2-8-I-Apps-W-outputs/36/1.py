
n, k = map(int, input().split())
p = list(map(int, input().split()))
buy = p[0]
sell = p[0] - k
profit = 0
for i in p:
  if i < buy:
    buy = i
  if i - buy > profit:
    sell = i
    profit = i - buy
print(profit * 100)

