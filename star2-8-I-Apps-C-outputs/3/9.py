
n = int(input())
b = [int(i) for i in input().split()]
left = [0 for i in range(n)]
right = [0 for i in range(n)]
max_damage = 0
max_index = 0

left[0] = b[0]
for i in range(1, n):
    left[i] = min(left[i-1], b[i])
right[n-1] = b[n-1]
for i in range(n-2, -1, -1):
    right[i] = min(right[i+1], b[i])
for i in range(1, n-1):
    damage = left[i-1] + right[i+1]
    if damage > max_damage:
        max_damage = damage
        max_index = i

print(max_damage, max_index)

