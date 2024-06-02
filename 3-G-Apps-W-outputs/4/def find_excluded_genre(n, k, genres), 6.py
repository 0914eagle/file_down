
def find_excluded_genre(n, k, genres):
    genre_counts = [0] * k
    stress_counts = [0] * k

    for i in range(n):
        genre_counts[genres[i] - 1] += 1
        if i > 0 and genres[i] != genres[i - 1]:
            stress_counts[genres[i - 1] - 1] += 1

    stress_counts[genres[-1] - 1] += 1

    min_stress = float('inf')
    excluded_genre = 1

    for i in range(k):
        total_stress = stress_counts[i] + genre_counts[i] - 1
        if total_stress < min_stress:
            min_stress = total_stress
            excluded_genre = i + 1

    return excluded_genre

# Input parsing
n, k = map(int, input().split())
genres = list(map(int, input().split()))

# Find and print the excluded genre
print(find_excluded_genre(n, k, genres))
