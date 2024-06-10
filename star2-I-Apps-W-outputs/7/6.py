
k = int(input())
vowels = "aeiou"
if k < 5:
    print(-1)
else:
    n = k // 5
    m = k // n
    if n * m != k:
        print(-1)
    else:
        word = ""
        for i in range(n):
            for j in range(m):
                word += vowels[(i + j) % 5]
        print(word)

