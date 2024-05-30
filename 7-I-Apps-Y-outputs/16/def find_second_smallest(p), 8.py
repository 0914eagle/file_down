
def find_second_smallest(p):
    # Write your code here
    if len(p) < 3:
        return 0
    p.sort()
    count = 0
    for i in range(1, len(p)-1):
        if p[i] == p[i-1] and p[i] == p[i+1]:
            continue
        elif p[i] == p[i-1] and p[i] != p[i+1]:
            count += 1
        elif p[i] != p[i-1] and p[i] == p[i+1]:
            count += 1
        else:
            count += 2
    return count

