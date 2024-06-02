
def song_at_moment(n, m, playlist, moments):
    total_duration = sum([c * t for c, t in playlist])
    song_times = [sum([c * t for c, t in playlist[:i]]) for i in range(1, n+1)]
    
    songs = []
    for moment in moments:
        time = moment % total_duration
        song = 1
        while time > song_times[song-1]:
            song += 1
        songs.append(song)
    
    return songs

# Input
n, m = map(int, input().split())
playlist = [list(map(int, input().split())) for _ in range(n)]
moments = list(map(int, input().split()))

# Output
result = song_at_moment(n, m, playlist, moments)
for song in result:
    print(song)
