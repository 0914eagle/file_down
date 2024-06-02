
def song_playing(n, m, playlist, moments):
    total_duration = sum([c * t for c, t in playlist])
    song_times = []
    current_time = 0
    for c, t in playlist:
        for _ in range(c):
            current_time += t
            song_times.append(current_time)
    
    result = []
    for moment in moments:
        for i, time in enumerate(song_times):
            if moment <= time:
                result.append(i + 1)
                break
    
    return result

# Input parsing
n, m = map(int, input().split())
playlist = [list(map(int, input().split())) for _ in range(n)]
moments = list(map(int, input().split()))

# Call the function and print the output
output = song_playing(n, m, playlist, moments)
for song_number in output:
    print(song_number)
