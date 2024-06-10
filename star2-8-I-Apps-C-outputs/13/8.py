
N, E, D = map(int, input().split())
ek = list(map(int, input().split()))
defuse = list(map(int, input().split()))
ek.sort()
defuse.sort()
winner = -1
idx_ek = 0
idx_defuse = 0
last_idx_ek = 0
last_idx_defuse = 0
while idx_ek < E and idx_defuse < D:
    if ek[idx_ek] < defuse[idx_defuse]:
        last_idx_ek = idx_ek
        idx_ek += 1
    else:
        last_idx_defuse = idx_defuse
        idx_defuse += 1
if idx_ek == E:
    winner = last_idx_defuse % N
else:
    winner = last_idx_ek % N
print(winner)

