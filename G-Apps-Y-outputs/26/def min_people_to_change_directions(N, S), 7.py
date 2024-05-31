
def min_people_to_change_directions(N, S):
    num_people_to_change = [0] * N
    num_people_to_change[0] = S.count('E')
    
    for i in range(1, N):
        if S[i-1] == 'E':
            num_people_to_change[i] = num_people_to_change[i-1] - 1
        else:
            num_people_to_change[i] = num_people_to_change[i-1]
        
        if S[i] == 'W':
            num_people_to_change[i] += 1
    
    return min(num_people_to_change)

# Input
N = int(input())
S = input().strip()

# Output
print(min_people_to_change_directions(N, S))
