
import sys
import itertools

def possible_strings(n, q, operations):
    if n == 1:
        return 6
    else:
        result = 0
        for i in range(q):
            a = operations[i][0]
            b = operations[i][1]
            for s in itertools.permutations(a):
                result += possible_strings(n-1, q, operations)
        return result

def main():
    n, q = map(int, sys.stdin.readline().split())
    operations = []
    for i in range(q):
        a, b = sys.stdin.readline().split()
        operations.append((a, b))
    result = possible_strings(n, q, operations)
    print(result)


if __name__ == '__main__':
    main()

