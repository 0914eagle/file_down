
def vowelly_word(k):
    vowels = "aeiou"
    n, m = -1, -1
    for i in range(1, k + 1):
        if k % i == 0 and i >= 5 and k // i >= 5:
            n, m = i, k // i
            break
    if n == -1:
        print(-1)
    else:
        vowelly_word = ""
        for i in range(n):
            for j in range(m):
                vowelly_word += vowels[(i + j) % 5]
        print(vowelly_word)

k = int(input())
vowelly_word(k)
```
