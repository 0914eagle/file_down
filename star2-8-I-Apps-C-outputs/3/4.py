
n = int(input())
b = list(map(int, input().split()))
max_damage = 0
for i in range(1, n-1):
damage = 0
for j in range(i):
damage += b[j]//2
for j in range(i+1, n):
damage += b[j]//2
if damage > max_damage:
max_damage = damage
max_index = i
print(max_damage, max_index)

