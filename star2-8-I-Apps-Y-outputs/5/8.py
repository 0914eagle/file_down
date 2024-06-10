
n, c = map(int, input().split())
w = list(map(int, input().split()))

eaten = 0
total = 0

for fruit in w:
	if total + fruit <= c:
		total += fruit
		eaten += 1

print(eaten)

