
X = int(input())
count = X // 500
happiness = count * 1000
X -= count * 500
count = X // 5
happiness += count * 5
print(happiness)

