
def solve():
    N = int(input())
    A = list(map(int, input().split()))
    m = 2*N
    for i in range(1,N):
        if A[i-1] > A[i]:
            m = 2*(N-i)
            break
    print(m)
    for i in range(1,N):
        for j in range(i,N):
            print(i,j+1)
            print(j+1,j+1)

solve()
