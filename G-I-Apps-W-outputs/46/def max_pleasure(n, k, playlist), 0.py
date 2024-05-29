
def max_pleasure(n, k, playlist):
    playlist.sort(key=lambda x: x[1], reverse=True)  # Sort songs by beauty in descending order
    max_pleasure = 0
    total_length = 0
    min_beauty = float('inf')
    
    for i in range(n):
        total_length += playlist[i][0]  # Add length of current song to total length
        min_beauty = min(min_beauty, playlist[i][1])  # Update min beauty so far
        
        if i >= k:  # If we exceed the limit of songs to choose, remove song with lowest beauty
            total_length -= playlist[i-k][0]
        
        max_pleasure = max(max_pleasure, total_length * min_beauty)  # Calculate and update max pleasure
    
    return max_pleasure

# Input processing
n, k = map(int, input().split())
playlist = [list(map(int, input().split())) for _ in range(n)]

# Output
print(max_pleasure(n, k, playlist))
```
