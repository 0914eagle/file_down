
def min_moves_to_divisible(a, b):
    if a % b == 0:
        return 0
    else:
        return b - (a % b)

# Read the number of test cases
t = int(input())

# Iterate through the test cases
for _ in range(t):
    a, b = map(int, input().split())
    print(min_moves_to_divisible(a, b))
