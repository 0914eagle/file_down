
def main():
    n = int(input())
    points = []
    for _ in range(n):
        x, y, z = [int(v) for v in input().split()]
        points.append((x, y, z))
    for i in range(1, n):
        print(i, i + 1)

if __name__ == "__main__":
    main()
