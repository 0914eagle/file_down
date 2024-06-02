
def count_missed_fogs(n, fogs):
    total_missed = 0
    nets = []
    
    for i in range(n):
        m, d, l, r, h, dd, dx, dh = fogs[i]
        fogs_generated = 0
        
        for k in range(m):
            fog_x1 = l + k * dx
            fog_x2 = r + k * dx
            fog_h = h + k * dh
            fog_d = d + k * dd
            
            caught = False
            for net in nets:
                if net[0] <= fog_x1 and net[1] >= fog_x2 and net[2] >= fog_h:
                    caught = True
                    break
            
            if not caught:
                total_missed += 1
                nets.append((fog_x1, fog_x2, fog_h))
    
    return total_missed

# Input parsing
n = int(input())
fogs = []
for _ in range(n):
    fogs.append(list(map(int, input().split())))

# Call the function and output the result
print(count_missed_fogs(n, fogs))
