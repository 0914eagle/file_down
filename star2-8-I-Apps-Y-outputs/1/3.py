
n, k = map(int, input().split())
arr = list(map(int, input().split()))
freq = {}
for elem in arr:
    if elem in freq:
        freq[elem] += 1
    else:
        freq[elem] = 1
if len(freq) < k:
    print("NO")
else:
    print("YES")
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    color = {}
    for i in range(k):
        color[freq[i][0]] = i + 1
    res = []
    for elem in arr:
        res.append(color[elem])
    print(" ".join(map(str, res)))

