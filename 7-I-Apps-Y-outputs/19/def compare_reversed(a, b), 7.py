
def compare_reversed(a, b):
    return str(max(a, b))[::-1]


def main():
    a, b = [int(x) for x in input().split()]
    print(compare_reversed(a, b))


if __name__ == "__main__":
    main()

