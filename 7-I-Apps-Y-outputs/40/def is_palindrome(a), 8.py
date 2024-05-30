
def is_palindrome(a):
    for i in range(len(a)):
        if a[i] != a[len(a) - 1 - i]:
            return False
    return True

def is_subpalindrome(a):
    for i in range(len(a)):
        for j in range(i + 2, len(a) + 1):
            if is_palindrome(a[i:j]):
                return True
    return False

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        if is_subpalindrome(a):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()

