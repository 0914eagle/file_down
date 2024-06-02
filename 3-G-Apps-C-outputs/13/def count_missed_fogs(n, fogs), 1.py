
def count_missed_fogs(n, fogs):
    total_missed_fogs = 0
    nets = []
    
    for i in range(n):
        m_i, d_i, l_i, r_i, h_i, delta_d_i, delta_x_i, delta_h_i = fogs[i]
        
        for k in range(m_i):
            fog_x_left = l_i + k * delta_x_i
            fog_x_right = r_i + k * delta_x_i
            fog_height = h_i + k * delta_h_i
            fog_day = d_i + k * delta_d_i
            
            missed = True
            for net in nets:
                if net[0] <= fog_x_left and net[1] >= fog_x_right and net[2] >= fog_height:
                    missed = False
                    break
            
            if missed:
                total_missed_fogs += 1
                nets.append((fog_x_left, fog_x_right, fog_height))
    
    return total_missed_fogs

# Input
n = int(input())
fogs = []
for _ in range(n):
    fogs.append(list(map(int, input().split())))

# Output
print(count_missed_fogs(n, fogs))
