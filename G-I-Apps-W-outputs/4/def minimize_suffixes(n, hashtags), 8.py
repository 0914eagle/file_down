
def minimize_suffixes(n, hashtags):
    hashtags.sort()
    shortest_hashtags = []
    
    for i in range(n-1):
        shortest = hashtags[i]
        next_shortest = hashtags[i+1]
        j = 1
        while j < min(len(shortest), len(next_shortest)) and shortest[j] == next_shortest[j]:
            j += 1
        shortest_hashtags.append(shortest[:j])
    
    shortest_hashtags.append(hashtags[-1])
    
    return shortest_hashtags

# Input
n = int(input())
hashtags = []
for _ in range(n):
    hashtags.append(input())

# Output
result = minimize_suffixes(n, hashtags)
for hashtag in result:
    print(hashtag)
```
