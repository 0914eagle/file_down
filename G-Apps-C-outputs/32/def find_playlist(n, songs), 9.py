
def find_playlist(n, songs):
    def backtrack(curr_playlist):
        if len(curr_playlist) == 9:
            return curr_playlist

        last_song = curr_playlist[-1]
        for next_song in songs[last_song]:
            if next_song not in curr_playlist:
                new_playlist = curr_playlist + [next_song]
                result = backtrack(new_playlist)
                if result:
                    return result

    for start_song in range(1, n + 1):
        playlist = [start_song]
        result = backtrack(playlist)
        if result:
            return result

    return "fail"

# Input parsing
n = int(input())
songs = {}
for i in range(1, n + 1):
    artist, t, *next_songs = input().split()
    songs[i] = [int(song) for song in next_songs]

# Find playlist
result = find_playlist(n, songs)
if result == "fail":
    print("fail")
else:
    print(*result)
