
def optimal_hashtags(n, hashtags):
    result = []
    for hashtag in hashtags:
        if len(result) == 0:
            result.append(hashtag)
        else:
            new_hashtag = ''
            for i in range(min(len(result[-1]), len(hashtag))):
                if result[-1][i] != hashtag[i]:
                    break
                new_hashtag += result[-1][i]
            new_hashtag += '#'
            result.append(new_hashtag)
    return result

# Input parsing
n = int(input())
hashtags = []
for _ in range(n):
    hashtags.append(input())

# Call the function to get the optimal hashtags
result = optimal_hashtags(n, hashtags)

# Output the result
for r in result:
    print(r)
```
