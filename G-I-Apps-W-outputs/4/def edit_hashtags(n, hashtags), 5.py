
def edit_hashtags(n, hashtags):
    edited_hashtags = []
    
    for i in range(n):
        hashtag = hashtags[i]
        j = 1
        while j < len(hashtag) and hashtag[j] >= hashtag[j-1]:
            j += 1
        edited_hashtags.append(hashtag[:j])
    
    return edited_hashtags

# Read input
n = int(input())
hashtags = [input().strip() for _ in range(n)]

# Call the function and print the output
result = edit_hashtags(n, hashtags)
for hashtag in result:
    print(hashtag)
```
