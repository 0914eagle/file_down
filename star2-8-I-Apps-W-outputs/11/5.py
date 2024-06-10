
import sys
def solve(n, k):
    result = 0
    for i in range(n):
        if k > 0:
            result |= (1 << i)
            k -= 1
    return result
if __name__ == "__main__":
    n, k = map(int, input().split())
    print(solve(n, k))

