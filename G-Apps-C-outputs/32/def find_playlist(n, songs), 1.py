
def find_playlist(n, songs):
    def find_next_song(curr_song, visited, playlist):
        nonlocal songs
        
        visited.add(curr_song)
        playlist.append(curr_song)
        
        if len(playlist) == 9:
            return True
        
        for next_song in songs[curr_song][1]:
            if next_song not in visited:
                if find_next_song(next_song, visited, playlist):
                    return True
        
        visited.remove(curr_song)
        playlist.pop()
        return False
    
    for start_song in range(1, n+1):
        visited = set()
        playlist = []
        
        if find_next_song(start_song, visited, playlist):
            return playlist
    
    return "fail"

# Input parsing
n = int(input())
songs = {}
for i in range(1, n+1):
    artist, t, *next_songs = input().split()
    next_songs = list(map(int, next_songs))
    songs[i] = (artist, next_songs)

# Find the playlist
result = find_playlist(n, songs)
if result == "fail":
    print(result)
else:
    print(*result)
