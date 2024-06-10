
def solve(k):
    if k == 1:
        return -1
    vowels = "aeiou"
    n = 1
    while n * n < k:
        n += 1
    m = k // n
    word = ""
    for i in range(n):
        for j in range(m):
            word += vowels[(i + j) % 5]
    return word

k = int(input())
print(solve(k))

