
import sys
import math

def solve(n, q, operations):
    result = 0
    return result

def main():
    n, q = map(int, input().split())
    operations = []
    for _ in range(q):
        a, b = input().split()
        operations.append((a, b))
    
    result = solve(n, q, operations)
    print(result)

if __name__ == "__main__":
    main()


