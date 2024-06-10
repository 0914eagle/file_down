
def solve(k):
    if k < 5:
        return -1
    if k == 5:
        return "aeiou"
    n = 1
    while n * (k - n) != k:
        n += 1
    m = k // n
    vowels = "aeiou"
    word = ""
    for i in range(n):
        for j in range(m):
            word += vowels[(i + j) % 5]
    return word

k = int(input())
print(solve(k))

