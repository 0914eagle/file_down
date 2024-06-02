
def find_genre_to_exclude(n, k, genres):
    genre_counts = [0] * k
    stress_counts = [0] * k
    
    for i in range(n):
        genre_counts[genres[i] - 1] += 1
        if i > 0 and genres[i] != genres[i - 1]:
            stress_counts[genres[i - 1] - 1] += 1
    
    max_stress = max(stress_counts)
    min_genre = stress_counts.index(max_stress)
    
    return min_genre + 1

# Input
n, k = map(int, input().split())
genres = list(map(int, input().split()))

# Output
print(find_genre_to_exclude(n, k, genres))
