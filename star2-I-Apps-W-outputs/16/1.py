
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    freq = {}
    for x in a:
        freq[x] = freq.get(x, 0) + 1
    ans = len(freq)
    print(ans)

