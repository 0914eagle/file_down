
n = int(input())
x = list(map(int, input().split()))
x.sort()

def calc_stamina(p):
    stamina = 0
    for i in range(n):
        stamina += (x[i] - p) ** 2
    return stamina

min_stamina = float('inf')
for p in range(1, 101):
    min_stamina = min(min_stamina, calc_stamina(p))

print(min_stamina)

