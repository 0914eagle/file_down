
def is_palindrome(a):
    return a == a[::-1]

def is_subpalindrome(a):
    for i in range(len(a) - 2):
        for j in range(i + 3, len(a) + 1):
            if is_palindrome(a[i:j]):
                return True
    return False

def check_palindrome(a):
    for i in range(len(a) - 2):
        if is_subpalindrome(a[i:]):
            return True
    return False

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        if check_palindrome(a):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()

