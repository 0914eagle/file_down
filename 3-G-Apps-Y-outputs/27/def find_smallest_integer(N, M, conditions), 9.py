
def find_smallest_integer(N, M, conditions):
    for num in range(10**(N-1), 10**N):
        num_str = str(num)
        if len(num_str) != N:
            continue
        valid = True
        for s, c in conditions:
            if num_str[s-1] != str(c):
                valid = False
                break
        if valid:
            return num
    return -1

# Sample Input Parsing
N, M = map(int, input().split())
conditions = [tuple(map(int, input().split())) for _ in range(M)]

result = find_smallest_integer(N, M, conditions)
print(result)
