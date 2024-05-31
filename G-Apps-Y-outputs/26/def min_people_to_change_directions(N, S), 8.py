
def min_people_to_change_directions(N, S):
    cnt_left = 0
    cnt_right = S.count('E')

    min_changes = cnt_left + cnt_right

    for i in range(1, N):
        if S[i-1] == 'W':
            cnt_left += 1
        if S[i] == 'E':
            cnt_right -= 1
        min_changes = min(min_changes, cnt_left + cnt_right)

    return min_changes

# Read input from Standard Input
N = int(input())
S = input().strip()

# Call the function and print the result
print(min_people_to_change_directions(N, S))
