
def count_missed_fogs(n, fogs):
    total_missed_fogs = 0
    nets = []
    
    for i in range(n):
        m_i, d_i, l_i, r_i, h_i, delta_d_i, delta_x_i, delta_h_i = fogs[i]
        
        for k in range(m_i):
            fog_left = l_i + k * delta_x_i
            fog_right = r_i + k * delta_x_i
            fog_top = h_i + k * delta_h_i
            
            missed = True
            for net in nets:
                net_left, net_right, net_top = net
                if fog_left >= net_left and fog_right <= net_right and fog_top <= net_top:
                    missed = False
                    break
            
            if missed:
                total_missed_fogs += 1
                nets.append((fog_left, fog_right, fog_top))
    
    return total_missed_fogs

# Input parsing
n = int(input())
fogs = []
for _ in range(n):
    fog_params = list(map(int, input().split()))
    fogs.append(fog_params)

# Call the function and output the result
result = count_missed_fogs(n, fogs)
print(result)
