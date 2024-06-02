
def check_pairwise_distinct(N, A):
    if len(set(A)) == len(A):
        print("YES")
    else:
        print("NO")

# Read input
N = int(input())
A = list(map(int, input().split()))

# Call the function
check_pairwise_distinct(N, A)
