
def min_people_to_change_directions(N, S):
    count_west = S.count('W')
    count_east = 0
    min_changes = count_west
    for direction in S:
        if direction == 'E':
            count_east += 1
        else:
            count_west -= 1
        changes_required = count_west + count_east
        if changes_required < min_changes:
            min_changes = changes_required
    return min_changes

# Reading input
N = int(input())
S = input().strip()

# Call the function and print the result
print(min_people_to_change_directions(N, S))
