
def song_at_moment(n, m, playlist, moments):
    total_duration = sum([c * t for c, t in playlist])
    current_duration = 0
    song_number = 0
    result = []

    for moment in moments:
        while current_duration + playlist[song_number][0] * playlist[song_number][1] < moment:
            current_duration += playlist[song_number][0] * playlist[song_number][1]
            song_number += 1

        result.append(song_number + 1)

    return result

# Input processing
n, m = map(int, input().split())
playlist = [list(map(int, input().split())) for _ in range(n)]
moments = list(map(int, input().split()))

# Call the function and print the output
output = song_at_moment(n, m, playlist, moments)
for song_number in output:
    print(song_number)