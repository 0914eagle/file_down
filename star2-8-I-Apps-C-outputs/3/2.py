
def solve(n, bs):
    max_damage = 0
    pillar = 0
    for i, b in enumerate(bs):
        damage = n - 2 - i
        max_damage = max(max_damage, damage)
        pillar = i
    return max_damage, pillar

n = int(input())
bs = list(map(int, input().split()))
max_damage, pillar = solve(n, bs)
print(max_damage, pillar)

