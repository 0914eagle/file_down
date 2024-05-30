
def count_second_smallest(p):
    count = 0
    for i in range(1, len(p) - 1):
        if p[i] == min(p[i - 1], p[i + 1]):
            count += 1
    return count

