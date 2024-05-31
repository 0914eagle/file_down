
def find_playlist(songs):
    def dfs(current_playlist):
        if len(current_playlist) == 9:
            return current_playlist
        
        current_song = current_playlist[-1]
        next_song_indices = songs[current_song][1]
        
        for next_song_index in next_song_indices:
            if next_song_index not in current_playlist:
                new_playlist = dfs(current_playlist + [next_song_index])
                if new_playlist:
                    return new_playlist
                
        return None
    
    for song_index in range(1, len(songs) + 1):
        playlist = dfs([song_index])
        if playlist:
            return playlist
    
    return "fail"

# Input
n = int(input())
songs = {}
for i in range(n):
    artist, t, *next_songs = input().split()
    next_songs = list(map(int, next_songs))
    songs[i + 1] = (artist, next_songs)

# Output
result = find_playlist(songs)
if result == "fail":
    print("fail")
else:
    print(*result)
