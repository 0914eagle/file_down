
def song_number(n, m, playlist, moments):
    total_duration = sum(c * t for c, t in playlist)
    current_time = 0
    song_index = 0
    result = []

    for moment in moments:
        while current_time + playlist[song_index][0] * playlist[song_index][1] < moment:
            current_time += playlist[song_index][0] * playlist[song_index][1]
            song_index += 1

        result.append(song_index + 1)

    return result

# Input parsing
n, m = map(int, input().split())
playlist = [tuple(map(int, input().split())) for _ in range(n)]
moments = list(map(int, input().split()))

# Call the function and print the output
output = song_number(n, m, playlist, moments)
for song in output:
    print(song)
