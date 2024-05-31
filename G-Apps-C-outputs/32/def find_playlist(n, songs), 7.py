
def find_playlist(n, songs):
    def backtrack(curr_playlist, visited):
        if len(curr_playlist) == 9:
            return curr_playlist
        for next_song in songs[curr_playlist[-1]]:
            if next_song not in visited:
                visited.add(next_song)
                result = backtrack(curr_playlist + [next_song], visited)
                if result:
                    return result
                visited.remove(next_song)
        return None

    for i in range(n):
        visited = set()
        visited.add(i)
        result = backtrack([i], visited)
        if result:
            return result
    return "fail"

# Input
n = int(input())
songs = {}
for i in range(n):
    artist, t, *next_songs = input().split()
    songs[i] = [int(s) - 1 for s in next_songs]

# Output
result = find_playlist(n, songs)
if result == "fail":
    print("fail")
else:
    print(" ".join(str(s + 1) for s in result))
