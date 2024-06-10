
n = int(input())
pieces = [int(x) for x in input().split()]
pieces.sort()

best = 360
left_sum = 0
right_sum = sum(pieces)

for p in pieces:
    left_sum += p
    right_sum -= p
    best = min(best, abs(left_sum - right_sum))

print(best)

