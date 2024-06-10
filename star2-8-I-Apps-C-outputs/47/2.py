
n, m = map(int, input().split())
species = {}
for _ in range(n):
    s, x = map(float, input().split())
    species[x] = s

count = 0
last = 0
for x in species:
    if species[x] != last:
        count += 1
    last = species[x]

print(count - 1)

