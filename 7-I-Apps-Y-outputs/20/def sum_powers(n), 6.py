

def sum_powers(n):
    # n = number of numbers
    # input: n numbers
    # output: sum of numbers
    # 1. read input
    # 2. calculate sum of numbers
    # 3. return sum
    return 0

def main():
    # read number of numbers
    n = int(input())
    # read numbers
    numbers = []
    for i in range(n):
        numbers.append(int(input()))
    # calculate sum of numbers
    sum = sum_powers(n, numbers)
    # print sum
    print(sum)

if __name__ == "__main__":
    main()

