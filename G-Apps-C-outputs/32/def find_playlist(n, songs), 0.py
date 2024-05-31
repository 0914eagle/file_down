
def find_playlist(n, songs):
    def dfs(curr_playlist):
        if len(curr_playlist) == 9:
            return curr_playlist
        
        curr_song = curr_playlist[-1]
        next_songs = songs[curr_song][1]
        
        for next_song in next_songs:
            if next_song not in curr_playlist:
                new_playlist = dfs(curr_playlist + [next_song])
                if new_playlist:
                    return new_playlist
        
        return None

    for i in range(n):
        playlist = dfs([i])
        if playlist:
            return playlist

    return "fail"

# Input
n = 10
songs = {
    0: ('a', [10, 3]),
    1: ('b', [6]),
    2: ('c', [1, 5]),
    3: ('d', [9]),
    4: ('e', [4]),
    5: ('f', [2]),
    6: ('g', [6, 8]),
    7: ('h', []),
    8: ('i', [3]),
    9: ('j', [7])
}

# Output
print(*find_playlist(n, songs))
