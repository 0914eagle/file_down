
def compare(a, b):
    if a == b:
        return a
    elif a > b:
        return b
    else:
        return a


def main():
    a = int(input())
    b = int(input())
    print(compare(a, b))


if __name__ == "__main__":
    main()

