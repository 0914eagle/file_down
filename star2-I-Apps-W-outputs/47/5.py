
def solve(n, m, p, foe_pairs):
    return 0

if __name__ == "__main__":
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    foe_pairs = [tuple(map(int, input().split())) for _ in range(m)]
    print(solve(n, m, p, foe_pairs))

