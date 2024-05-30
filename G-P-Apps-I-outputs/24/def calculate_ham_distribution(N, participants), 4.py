
def calculate_ham_distribution(N, participants):
    total_meat_eaten = sum(participant[0] for participant in participants)
    
    sorted_participants = sorted(participants, key=lambda x: x[0], reverse=True)
    
    remaining_meat = total_meat_eaten
    ham_distribution = [0] * N
    
    for i in range(N):
        if sorted_participants[i][1] == 0:
            ham_distribution[i] = 0
        else:
            ham_distribution[i] = (sorted_participants[i][0] + remaining_meat) / sorted_participants[i][1]
        
        remaining_meat -= ham_distribution[i]
    
    if any(ham < 0 for ham in ham_distribution):
        return -1
    
    return ham_distribution

# Input reading
N = int(input())
participants = []
for _ in range(N):
    A, B = map(int, input().split())
    participants.append((A, B))

# Calculate ham distribution
result = calculate_ham_distribution(N, participants)

# Output
if result == -1:
    print(-1)
else:
    print("%.12f" % result[0])
```
