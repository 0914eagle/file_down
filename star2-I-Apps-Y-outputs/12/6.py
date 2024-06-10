
N = int(input())
A = list(map(int, input().split()))

def reconstruct(N, A):
    order = [0] * N
    for i in range(N):
        order[A[i] - 1] = i + 1
    return order

print(*reconstruct(N, A))

