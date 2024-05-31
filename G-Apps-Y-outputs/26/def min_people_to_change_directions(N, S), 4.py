
def min_people_to_change_directions(N, S):
    num_west = S.count('W')
    num_east = N - num_west
    min_changes = min(num_west, num_east)
    return min_changes

# Read input from Standard Input
N = int(input())
S = input().strip()

# Call the function and print the output
print(min_people_to_change_directions(N, S))
