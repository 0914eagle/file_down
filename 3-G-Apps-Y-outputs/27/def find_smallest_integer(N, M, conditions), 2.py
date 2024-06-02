
def find_smallest_integer(N, M, conditions):
    for num in range(10**(N-1), 10**N):
        num_str = str(num)
        if all(num_str[s-1] == str(c) for s, c in conditions):
            return num
    return -1

# Input processing
N, M = map(int, input().split())
conditions = [tuple(map(int, input().split())) for _ in range(M)]

# Call the function and print the result
result = find_smallest_integer(N, M, conditions)
print(result)
