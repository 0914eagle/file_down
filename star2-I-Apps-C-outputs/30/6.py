
def bipartite_battle(n, a, b):
    pass

if __name__ == '__main__':
    n = int(input())
    a = []
    b = []
    for _ in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    print(bipartite_battle(n, a, b))

