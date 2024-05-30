


def shovels(n, k):
    # your code goes here
    if n == 1:
        return 1
    if n <= k:
        return n
    if n > k:
        return k + shovels(n - k, k)


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(shovels(n, k))


