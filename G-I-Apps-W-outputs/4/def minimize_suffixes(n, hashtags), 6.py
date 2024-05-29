
def minimize_suffixes(n, hashtags):
    result = []
    for hashtag in hashtags:
        if len(result) == 0:
            result.append(hashtag)
        else:
            common_len = min(len(result[-1]), len(hashtag))
            i = 1
            while i < common_len and result[-1][i] == hashtag[i]:
                i += 1
            result[-1] = result[-1][:i]
            result.append(hashtag)
    
    for hashtag in result:
        print(hashtag)

# Example usage
n = 3
hashtags = ['#book', '#bigtown', '#big']
minimize_suffixes(n, hashtags)
```
