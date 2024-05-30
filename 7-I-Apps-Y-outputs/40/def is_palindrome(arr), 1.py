
def is_palindrome(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] != arr[n - i - 1]:
            return False
    return True

def is_subpalindrome(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 2, n + 1):
            if is_palindrome(arr[i:j]):
                return True
    return False

def check(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 2, n + 1):
            if is_palindrome(arr[i:j]):
                return "YES"
    return "NO"

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(check(arr))

