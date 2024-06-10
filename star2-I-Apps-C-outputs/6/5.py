
def main():
    B = int(input())
    H = int(input())
    R, C = map(int, input().split())
    grid = [input() for _ in range(R)]
    total_cost = 0
    for r in range(R):
        for c in range(C):
            s = int(grid[r][c])
            if s < B:
                total_cost += 11
            else:
                total_cost += 43
    print(total_cost)

if __name__ == "__main__":
    main()

