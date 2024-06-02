
def check_pairwise_distinct(N, A):
    if len(set(A)) == N:
        print("YES")
    else:
        print("NO")

# Input processing
N = int(input())
A = list(map(int, input().split()))

check_pairwise_distinct(N, A)
