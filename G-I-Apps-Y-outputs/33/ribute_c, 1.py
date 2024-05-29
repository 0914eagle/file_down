ribute_crackers(N, K):
    return N % K

N, K = map(int, input().split())
result = distribute_crackers(N, K)
print(result