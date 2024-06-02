
def solve(R, C, grid):
    # TODO: solve the problem

def main():
    R, C = map(int, input().split())
    grid = []
    for _ in range(R):
        grid.append(input())
    print(solve(R, C, grid))

if __name__ == '__main__':
    main()

