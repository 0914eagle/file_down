
from collections import Counter

def count_ways_to_choose_three_people(N, names):
    count = Counter([name[0] for name in names])

    M_count = count['M']
    A_count = count['A']
    R_count = count['R']
    C_count = count['C']
    H_count = count['H']

    ways = 0
    ways += M_count * A_count * R_count
    ways += M_count * A_count * C_count
    ways += M_count * A_count * H_count
    ways += M_count * R_count * C_count
    ways += M_count * R_count * H_count
    ways += M_count * C_count * H_count
    ways += A_count * R_count * C_count
    ways += A_count * R_count * H_count
    ways += A_count * C_count * H_count
    ways += R_count * C_count * H_count

    return ways // 6

# Input processing
N = int(input())
names = [input() for _ in range(N)]

# Count ways to choose three people
result = count_ways_to_choose_three_people(N, names)
print(result)
