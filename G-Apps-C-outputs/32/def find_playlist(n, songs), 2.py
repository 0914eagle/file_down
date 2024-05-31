
def find_playlist(n, songs):
    def dfs(path):
        if len(path) == 9:
            return path
        curr_song = path[-1]
        for next_song in songs[curr_song][1]:
            if next_song not in path and all(songs[next_song][0] != songs[song][0] for song in path):
                new_path = dfs(path + [next_song])
                if new_path:
                    return new_path
        return []
    
    for start_song in range(1, n+1):
        playlist = dfs([start_song])
        if playlist:
            return playlist
    return ['fail']

# Input processing
n = int(input())
songs = {}
for i in range(1, n+1):
    artist, t, *related_songs = input().split()
    songs[i] = (artist, list(map(int, related_songs)))

# Find playlist
result = find_playlist(n, songs)
print(*result)
