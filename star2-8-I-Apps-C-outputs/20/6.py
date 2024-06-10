
import sys


def readline():
    return sys.stdin.readline().strip()


def readlines():
    return sys.stdin.readlines()


def solve():
    rebus = readline().split()
    n = int(rebus[-1])
    num_q = rebus.count("?")
    if num_q % 2 == 1:
        return "Impossible"
    max_sum = n * num_q // 2
    left = 0
    right = n
    while left < right:
        mid = (left + right) // 2
        if mid <= max_sum:
            left = mid + 1
        else:
            right = mid
    target = left - 1
    if target % 2 == 1:
        return "Impossible"
    left = 0
    right = n
    while left < right:
        mid = (left + right) // 2
        if mid <= target // 2:
            left = mid + 1
        else:
            right = mid
    first = left - 1
    second = target - first
    left = 0
    right = n
    while left < right:
        mid = (left + right) // 2
        if mid <= second:
            left = mid + 1
        else:
            right = mid
    third = left - 1
    fourth = second - third
    solution = [first, second, third, fourth]
    signs = ["+", "-", "+"]
    result = ""
    for i in range(num_q):
        result += str(solution[i]) + " " + signs[i] + " "
    result += str(solution[-1]) + " = " + str(n)
    return result


if __name__ == "__main__":
    print(solve())

