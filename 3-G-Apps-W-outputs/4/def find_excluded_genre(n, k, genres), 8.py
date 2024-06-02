
def find_excluded_genre(n, k, genres):
    genre_count = [0] * k
    stress_count = [0] * k

    for i in range(n):
        genre_count[genres[i] - 1] += 1
        if i > 0 and genres[i] != genres[i - 1]:
            stress_count[genres[i - 1] - 1] += 1

    stress_count[genres[-1] - 1] += 1

    min_stress = float('inf')
    excluded_genre = 0
    for i in range(k):
        total_stress = stress_count[i] + genre_count[i] - 1
        if total_stress < min_stress:
            min_stress = total_stress
            excluded_genre = i + 1

    return excluded_genre

# Input parsing
n, k = map(int, input().split())
genres = list(map(int, input().split()))

# Call the function and print the output
print(find_excluded_genre(n, k, genres))
