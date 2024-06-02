
def count_missed_fogs(n, fogs):
    missed_fogs = 0
    nets = []
    
    for _ in range(n):
        m, d, l, r, h, dd, dx, dh = fogs.pop(0)
        fogs_positions = [(l, r, h)]
        
        for _ in range(m-1):
            l += dx
            r += dx
            h += dh
            fogs_positions.append((l, r, h))
        
        for fog in fogs_positions:
            missed = True
            for net in nets:
                if fog[0] >= net[0] and fog[1] <= net[1] and fog[2] <= net[2]:
                    missed = False
                    break
            if missed:
                missed_fogs += 1
                nets.append(fog)
    
    return missed_fogs

# Input parsing
n = int(input())
fogs = []
for _ in range(n):
    fogs.append(list(map(int, input().split())))

# Calculate and output the result
print(count_missed_fogs(n, fogs))
