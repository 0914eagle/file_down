
def minesweeper(n):
    return 4*n+4

def main():
    n = int(input())
    print(minesweeper(n))
    print(' '.join(map(str, range(1, 4*n+5))))

if __name__ == "__main__":
    main()

