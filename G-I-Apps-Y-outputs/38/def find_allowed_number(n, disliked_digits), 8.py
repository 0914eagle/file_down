
def find_allowed_number(n, disliked_digits):
    while True:
        n_str = str(n)
        if all(digit not in disliked_digits for digit in n_str):
            return n
        n += 1

if __name__ == "__main__":
    N, K = map(int, input().split())
    disliked_digits = input().split()
    
    ans = find_allowed_number(N, disliked_digits)
    print(ans)
```
