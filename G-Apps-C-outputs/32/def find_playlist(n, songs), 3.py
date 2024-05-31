
def find_playlist(n, songs):
    def backtrack(current_playlist):
        if len(current_playlist) == 9:
            return current_playlist

        last_song = current_playlist[-1]
        next_songs = songs[last_song]
        for next_song in next_songs:
            if next_song not in current_playlist:
                new_playlist = current_playlist + [next_song]
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
    artist, t, *adjacent_songs = input().split()
    songs[i] = list(map(int, adjacent_songs))

# Output
result = find_playlist(n, songs)
if result == "fail":
    print("fail")
else:
    print(*result)
