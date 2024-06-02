
def count_missed_fogs(n, fogs):
    total_missed = 0
    nets = []

    for i in range(n):
        m, d, l, r, h, dd, dx, dh = fogs[i]

        for j in range(m):
            fog_x1 = l + j*dx
            fog_x2 = r + j*dx
            fog_h = h + j*dh
            fog_day = d + j*dd

            missed = True
            for net in nets:
                if fog_x1 >= net[0] and fog_x2 <= net[1] and fog_h <= net[3]:
                    missed = False
                    break

            if missed:
                total_missed += 1
                nets.append((fog_x1, fog_x2, fog_h, fog_day))

    return total_missed

# Input processing
n = int(input())
fogs = []
for _ in range(n):
    fogs.append(list(map(int, input().split())))

# Call the function and output the result
print(count_missed_fogs(n, fogs))
