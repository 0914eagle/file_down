
n = int(input())
pillars = [int(i) for i in input().split()]

damage = 1
max_damage = 1
destroyed = 0

for i in range(1, n-1):
if pillars[i] >= pillars[i-1] + pillars[i+1]:
damage += 1
if damage > max_damage:
max_damage = damage
destroyed = i
damage = 1

print(max_damage, destroyed)

