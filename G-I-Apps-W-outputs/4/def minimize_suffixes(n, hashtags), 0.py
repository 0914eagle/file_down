
def minimize_suffixes(n, hashtags):
    hashtags.sort()
    result = []
    for h in hashtags:
        i = 1
        while i < len(h) and h[i] == h[i-1]:
            i += 1
        result.append(h[:i])
    return result

n = int(input())
hashtags = [input().strip() for _ in range(n)]
result = minimize_suffixes(n, hashtags)
for r in result:
    print(r)
