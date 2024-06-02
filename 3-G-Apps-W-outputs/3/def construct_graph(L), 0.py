
def construct_graph(L):
    N = 2 * L
    M = 2 * L + 2
    print(N, M)
    
    for i in range(1, L):
        print(i, i + 1, 0)
        print(i, i + L, i - 1)
    
    print(L, L + 1, 0)
    print(L, L + L, L - 1)
    
    for i in range(1, L):
        print(i + L, i + L + 1, 1)
    
    print(L + L, N, 1)

L = int(input())
construct_graph(L)
