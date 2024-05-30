
def compare_numbers(num1, num2):
    return str(num1)[::-1] if num1 > num2 else str(num2)[::-1]


def main():
    num1, num2 = [int(i) for i in input().split()]
    print(compare_numbers(num1, num2))


if __name__ == "__main__":
    main()

