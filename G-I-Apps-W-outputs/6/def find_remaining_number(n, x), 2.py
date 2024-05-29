
def find_remaining_number(n, x):
    total_sum = n*(n+1)//2
    remaining_sum = n*(n+1)//2 - x
    return total_sum - remaining_sum

# Read the number of queries
T = int(input())

# Process each query
for _ in range(T):
    n, x = map(int, input().split())
    result = find_remaining_number(n, x)
    print(result)
