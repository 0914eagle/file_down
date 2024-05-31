
def find_playlist(n, songs):
    def backtrack(curr_playlist, visited):
        if len(curr_playlist) == 9:
            return curr_playlist
        for next_song in songs[curr_playlist[-1]]:
            if next_song not in visited:
                new_playlist = curr_playlist + [next_song]
                new_visited = visited.copy()
                new_visited.add(next_song)
                result = backtrack(new_playlist, new_visited)
                if result:
                    return result
        return None
    
    for i in range(n):
        playlist = backtrack([i], {i})
        if playlist:
            return playlist
    return "fail"

# Input reading
n = int(input())
songs = {}
for i in range(n):
    artist, t, *next_songs = input().split()
    songs[i] = [int(song) - 1 for song in next_songs]

# Finding playlist
result = find_playlist(n, songs)

# Output
if result == "fail":
    print("fail")
else:
    print(' '.join(str(song + 1) for song in result))
