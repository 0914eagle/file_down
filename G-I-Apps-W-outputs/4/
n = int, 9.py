
n = int(input())
hashtags = []
for _ in range(n):
    hashtag = input().strip()
    hashtags.append(hashtag)

result = []
prev_hashtag = ""
for hashtag in sorted(hashtags):
    common_len = 0
    while common_len < min(len(prev_hashtag), len(hashtag)) and prev_hashtag[common_len] == hashtag[common_len]:
        common_len += 1
    result.append("#" + hashtag[:common_len + 1])
    prev_hashtag = hashtag
print("\n".join(result))
```
