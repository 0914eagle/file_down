
n = int(input())
x = list(map(int, input().split()))
x.sort()

def calc_stamina(p):
    total_stamina = 0
    for xi in x:
        total_stamina += (xi - p)**2
    return total_stamina

min_stamina = float('inf')
for p in range(1, 101):
    min_stamina = min(min_stamina, calc_stamina(p))

print(min_stamina)

