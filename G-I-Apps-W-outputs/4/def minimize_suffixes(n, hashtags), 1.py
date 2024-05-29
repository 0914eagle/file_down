
def minimize_suffixes(n, hashtags):
    result = []
    prev_hashtag = ''
    for hashtag in sorted(hashtags):
        min_suffix = 0
        for i in range(min(len(prev_hashtag), len(hashtag))):
            if prev_hashtag[i] != hashtag[i]:
                break
            min_suffix += 1
        result.append(hashtag[:min_suffix + 1])
        prev_hashtag = hashtag
    return result

# Read input
n = int(input())
hashtags = [input().strip() for _ in range(n)]

# Call the function and print the output
output = minimize_suffixes(n, hashtags)
for hashtag in output:
    print(hashtag)
```
