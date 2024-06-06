
buyers, price = input().split()
buyers = int(buyers)
price = int(price)
total = 0
for i in range(buyers):
    answer = input()
    if answer == "half":
        total += price // 2
    elif answer == "halfplus":
        total += price // 2 + (price // 2)
print(total)
