
def find_playlist(n, songs):
    def backtrack(curr_playlist):
        nonlocal found_playlist

        if len(curr_playlist) == 9:
            found_playlist = curr_playlist.copy()
            return

        curr_song = curr_playlist[-1]
        next_songs = songs[curr_song][1]

        for next_song in next_songs:
            if next_song not in curr_playlist and not found_playlist:
                curr_playlist.append(next_song)
                backtrack(curr_playlist)
                curr_playlist.pop()

    found_playlist = []
    for start_song in range(1, n + 1):
        backtrack([start_song])
        if found_playlist:
            return found_playlist

    return ["fail"]

# Input parsing
n = int(input())
songs = {}
for i in range(1, n + 1):
    song_data = input().split()
    artist = song_data[0]
    num_next_songs = int(song_data[1])
    next_songs = [int(x) for x in song_data[2:]]
    songs[i] = (artist, next_songs)

# Finding playlist
result = find_playlist(n, songs)
print(*result)
