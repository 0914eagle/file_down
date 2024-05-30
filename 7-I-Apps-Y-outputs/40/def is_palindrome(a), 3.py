

def is_palindrome(a):
    return a == a[::-1]

def is_subpalindrome(a):
    for i in range(len(a)):
        for j in range(i + 2, len(a) + 1):
            if is_palindrome(a[i:j]):
                return True
    return False

def solve(a):
    return "YES" if is_subpalindrome(a) else "NO"


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(solve(a))

