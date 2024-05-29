
def count_almost_palindromic_substrings(s, l, r):
    count = 0
    for i in range(l - 1, r):
        count += 1
        left = i
        right = r - 1
        while left < right:
            if s[left] != s[right]:
                count += 1
            left += 1
            right -= 1
    return count

def main():
    n, q = map(int, input().split())
    s = input()
    
    for _ in range(q):
        l, r = map(int, input().split())
        result = count_almost_palindromic_substrings(s, l, r)
        print(result)

if __name__ == "__main__":
    main()
```
