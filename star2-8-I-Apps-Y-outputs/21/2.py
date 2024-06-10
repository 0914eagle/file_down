
X = int(input())
coin_kinds = [500, 100, 50, 10, 5, 1]
happy_points = 0
for coin_value in coin_kinds:
    num_coins = X // coin_value
    if coin_value == 500:
        happy_points += num_coins * 1000
    else:
        happy_points += num_coins * 5
    X -= num_coins * coin_value
print(happy_points)

