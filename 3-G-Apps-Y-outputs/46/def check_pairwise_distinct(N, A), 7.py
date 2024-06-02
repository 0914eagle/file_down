
def check_pairwise_distinct(N, A):
    unique_set = set()
    for num in A:
        if num in unique_set:
            return "NO"
        unique_set.add(num)
    return "YES"

# Input
N = int(input())
A = list(map(int, input().split()))

# Output
print(check_pairwise_distinct(N, A))
