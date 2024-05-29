
def count_almost_palindromic_substrings(s, l, r):
    def is_almost_palindromic(sub_s):
        return sub_s == sub_s[::-1] or sub_s[:len(sub_s)//2] == sub_s[-1:-len(sub_s)//2-1:-1]

    count = 0
    for i in range(l-1, r):
        for j in range(i, r):
            if is_almost_palindromic(s[i:j+1]):
                count += 1
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
