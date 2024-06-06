
def main():
    x, y = list(map(int, input().split()))
    v, w = list(map(float, input().split()))
    print(
        (max(abs(x), abs(y)) / v) +
        (2 * (abs(x) + abs(y)) / (v * w))
    )

if __name__ == '__main__':
    main()
