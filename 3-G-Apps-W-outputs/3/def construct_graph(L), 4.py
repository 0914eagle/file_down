
def construct_graph(L):
    N = 2 * L
    M = 2 * L + 2
    print(N, M)
    
    for i in range(1, L):
        print(i, i+1, 0)
        print(i, i+L, i-1)
    
    print(L, L+1, 0)
    print(L, L+L, L-1)
    print(1, L, 0)
    print(L, N, L-1)

L = int(input())
construct_graph(L)
