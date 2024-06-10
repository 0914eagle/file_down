
def next_permutation(n):
    n = list(str(n))
    i = len(n) - 1
    while i > 0:
        if n[i - 1] < n[i]:
            break
        i -= 1
    if i == 0:
        return 0
    j = len(n) - 1
    while n[j] <= n[i - 1]:
        j -= 1
    n[i - 1], n[j] = n[j], n[i - 1]
    n[i:] = n[len(n) - 1:i - 1:-1]
    return int("".join(n))

x = int(input())
print(next_permutation(x))

