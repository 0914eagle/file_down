
def minimize_suffixes(n, hashtags):
    sorted_hashtags = sorted(hashtags)
    result = []
    for h in hashtags:
        idx = sorted_hashtags.index(h)
        common_prefix = ""
        if idx > 0:
            for i in range(min(len(h), len(sorted_hashtags[idx-1]))):
                if h[i] == sorted_hashtags[idx-1][i]:
                    common_prefix += h[i]
                else:
                    break
        result.append("#" + common_prefix)
    return result

# Read input
n = int(input())
hashtags = []
for _ in range(n):
    hashtags.append(input().strip())

# Call the function and print the output
result = minimize_suffixes(n, hashtags)
for r in result:
    print(r)
```
