
def find_genre_to_exclude(n, k, genres):
    genre_count = [0] * k
    stress_count = [0] * k
    
    for i in range(n):
        genre_count[genres[i] - 1] += 1
        if i > 0 and genres[i] != genres[i - 1]:
            stress_count[genres[i - 1] - 1] += 1
    
    max_stress = max(stress_count)
    min_genre = stress_count.index(max_stress)
    
    return min_genre + 1

# Input parsing
n, k = map(int, input().split())
genres = list(map(int, input().split()))

# Call the function and print the result
print(find_genre_to_exclude(n, k, genres))
