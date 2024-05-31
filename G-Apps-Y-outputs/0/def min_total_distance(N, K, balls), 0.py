
def min_total_distance(N, K, balls):
    type_A_dist = 0
    type_B_dist = 0
    
    for x in balls:
        type_A_dist += min(x * 2, (K - x) * 2)
        type_B_dist += min(x * 2, (K - x) * 2)
    
    return min(type_A_dist, type_B_dist)

# Read inputs
N = int(input())
K = int(input())
balls = list(map(int, input().split()))

# Call the function and print the result
print(min_total_distance(N, K, balls))
