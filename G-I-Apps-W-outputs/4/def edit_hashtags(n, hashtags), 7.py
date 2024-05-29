
def edit_hashtags(n, hashtags):
    result = []
    
    for i in range(n - 1):
        current = hashtags[i]
        next_hashtag = hashtags[i + 1]
        j = 1
        
        while j < len(current) and j < len(next_hashtag) and current[j] == next_hashtag[j]:
            j += 1
        
        result.append(current[:j])
    
    result.append(hashtags[n - 1])
    
    for word in result:
        print(word)

# Input reading
n = int(input())
hashtags = [input().strip() for _ in range(n)]

# Call the function
edit_hashtags(n, hashtags)
```
