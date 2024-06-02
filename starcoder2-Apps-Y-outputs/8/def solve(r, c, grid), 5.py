
def solve(r, c, grid):
    # Write your code here.
    return "kala"

def main():
    r, c = map(int, input().split())
    grid = []
    for _ in range(r):
        grid.append(input())
    print(solve(r, c, grid))

if __name__ == "__main__":
    main()

