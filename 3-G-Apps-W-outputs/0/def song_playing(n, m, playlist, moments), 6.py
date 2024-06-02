
def song_playing(n, m, playlist, moments):
    total_duration = sum([c * t for c, t in playlist])
    current_time = 0
    song_number = 0
    result = []

    for moment in moments:
        while current_time + playlist[song_number][0] * playlist[song_number][1] < moment:
            current_time += playlist[song_number][0] * playlist[song_number][1]
            song_number += 1

        result.append(song_number + 1)

    return result

# Input
n, m = map(int, input().split())
playlist = [list(map(int, input().split())) for _ in range(n)]
moments = list(map(int, input().split()))

# Output
output = song_playing(n, m, playlist, moments)
for song in output:
    print(song)
