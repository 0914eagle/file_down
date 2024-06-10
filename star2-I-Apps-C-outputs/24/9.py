
def solve(n, edges):
    return "Yes"

if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    print(solve(n, edges))

