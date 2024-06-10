
import sys
input = sys.stdin.readline


def is_palindrome(arr):
    return arr == arr[::-1]


def solve(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 2, n + 1):
            if is_palindrome(arr[i:j]):
                return True
    return False


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print("YES" if solve(arr) else "NO")


if __name__ == "__main__":
    main()


