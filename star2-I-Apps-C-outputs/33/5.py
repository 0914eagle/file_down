
def solve(N, K, plants):
    pass

if __name__ == "__main__":
    N, K = map(int, input().split())
    plants = []
    for _ in range(N):
        X, Y, F = map(int, input().split())
        plants.append((X, Y, F))
    energy, path = solve(N, K, plants)
    print(energy)
    print(len(path))
    for x, y in path:
        print(x, y)

