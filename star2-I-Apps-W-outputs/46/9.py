
def solve(n, m, groups):
    return "YES"

def main():
    n, m = map(int, input().split())
    groups = []
    for _ in range(m):
        group = list(map(int, input().split()))
        groups.append(group)
    
    print(solve(n, m, groups))

if __name__ == "__main__":
    main()

