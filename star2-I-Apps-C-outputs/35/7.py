
def solve(n, a, b):
    cards = [0] * (n + 1)
    for i in range(n):
        cards[a[i]] = i + 1
    pile = [0] * (n + 1)
    for i in range(n):
        pile[b[i]] = i + 1
    pos = [0] * (n + 1)
    for i in range(1, n + 1):
        pos[cards[i]] = i
    ans = 0
    for i in range(1, n + 1):
        if cards[i] != i:
            ans += 1
            j = pile[i]
            while cards[j] != i:
                j = pile[j]
            cards[pos[i]] = cards[j]
            pos[cards[j]] = pos[i]
    return ans

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(solve(n, a, b))

