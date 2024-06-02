
def find_excluded_genre(n, k, genres):
    genre_counts = [0] * k
    stress_counts = [0] * k

    for i in range(n):
        genre_counts[genres[i] - 1] += 1
        if i > 0 and genres[i] != genres[i - 1]:
            stress_counts[genres[i - 1] - 1] += 1

    stress_counts[genres[-1] - 1] += 1

    min_stresses = float('inf')
    excluded_genre = 1

    for i in range(k):
        total_stresses = sum(stress_counts) - stress_counts[i] + genre_counts[i]
        if total_stresses < min_stresses:
            min_stresses = total_stresses
            excluded_genre = i + 1

    return excluded_genre

# Input parsing
n, k = map(int, input().split())
genres = list(map(int, input().split()))

# Call the function and print the output
print(find_excluded_genre(n, k, genres))
