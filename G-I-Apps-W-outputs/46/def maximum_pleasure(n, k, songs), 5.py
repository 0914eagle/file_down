
def maximum_pleasure(n, k, songs):
    songs.sort(key=lambda x: x[1], reverse=True)
    total_length = 0
    max_beauty = 0
    max_pleasure = 0
    
    for i in range(n):
        if i < k:
            total_length += songs[i][0]
            max_beauty = max(max_beauty, songs[i][1])
            max_pleasure = max(max_pleasure, total_length * max_beauty)
        else:
            break
    
    return max_pleasure

# Reading input
n, k = map(int, input().split())
songs = [list(map(int, input().split())) for _ in range(n)]

# Calling the function and printing the result
print(maximum_pleasure(n, k, songs))
