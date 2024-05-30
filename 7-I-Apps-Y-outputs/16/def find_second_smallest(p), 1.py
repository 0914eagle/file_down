
def find_second_smallest(p):
    if len(p) < 3:
        return 0
    count = 0
    for i in range(1, len(p) - 1):
        if p[i] > p[i - 1] and p[i] < p[i + 1]:
            count += 1
    return count

