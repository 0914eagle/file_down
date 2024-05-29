
def shorten_hashtags(n, hashtags):
    output = []
    
    hashtags.sort()
    longest_common_prefix = os.path.commonprefix(hashtags)
    
    for hashtag in hashtags:
        shortened_hashtag = '#' + longest_common_prefix
        output.append(shortened_hashtag)
    
    return output

n = int(input())
hashtags = []
for _ in range(n):
    hashtags.append(input())

result = shorten_hashtags(n, hashtags)
for shortened_hashtag in result:
    print(shortened_hashtag)
``` 

