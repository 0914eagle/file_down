
def solve(n, m, map):
    pass

def main():
    n, m = map(int, input().split())
    map = []
    for _ in range(n):
        map.append(input())
    
    t, map = solve(n, m, map)
    print(t)
    for row in map:
        print(row)

if __name__ == "__main__":
    main()

