
def find_playlist(songs, current_playlist, depth):
    if len(current_playlist) == 9:
        return current_playlist

    if depth == 0:
        return None

    for next_song in songs[current_playlist[-1]]:
        if next_song not in current_playlist:
            new_playlist = find_playlist(songs, current_playlist + [next_song], depth - 1)
            if new_playlist is not None:
                return new_playlist

    return None

n = int(input())
songs = {}
for i in range(1, n+1):
    artist, t, *next_songs = input().split()
    songs[i] = [int(song) for song in next_songs]

for start_song in range(1, n+1):
    playlist = find_playlist(songs, [start_song], 8)
    if playlist is not None:
        print(" ".join(str(song) for song in playlist))
        break
else:
    print("fail")
