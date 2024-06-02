
def count_missed_fogs(n, fogs):
    total_missed_fogs = 0
    nets = []

    for i in range(n):
        m_i, d_i, l_i, r_i, h_i, delta_d_i, delta_x_i, delta_h_i = fogs[i]

        for k in range(m_i):
            fog_x = l_i + k * delta_x_i
            fog_y = h_i + k * delta_h_i
            fog_day = d_i + k * delta_d_i

            missed = True
            for net in nets:
                if net[0] <= fog_x <= net[1] and net[2] <= fog_y:
                    missed = False
                    break

            if missed:
                total_missed_fogs += 1
                nets.append((l_i, r_i, h_i + (m_i - 1) * delta_h_i))

    return total_missed_fogs

# Read input
n = int(input())
fogs = []
for _ in range(n):
    fogs.append(list(map(int, input().split())))

# Calculate and output result
result = count_missed_fogs(n, fogs)
print(result)
