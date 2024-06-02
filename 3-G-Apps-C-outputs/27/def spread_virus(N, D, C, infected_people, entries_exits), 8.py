
def spread_virus(N, D, C, infected_people, entries_exits):
    infected = set(infected_people)
    contacts = [[] for _ in range(D+1)]
    
    for i in range(N):
        for j in range(i+1, N):
            if entries_exits[i][1] >= entries_exits[j][0] and entries_exits[j][1] >= entries_exits[i][0]:
                contacts[0].append((i+1, j+1))
    
    for day in range(1, D+1):
        for contact in contacts[day-1]:
            for i in range(N):
                if i+1 not in infected and (entries_exits[i][0] <= day and entries_exits[i][1] >= day):
                    contacts[day].append((contact[0], i+1))
                    contacts[day].append((contact[1], i+1))
                    infected.add(i+1)
    
    result = set()
    for contact in contacts[D]:
        result.add(contact[1])
    
    return sorted(result)

# Input parsing
N, D = map(int, input().split())
C, *infected_people = map(int, input().split())
entries_exits = [list(map(int, input().split())) for _ in range(N)]

# Call the function and print the output
output = spread_virus(N, D, C, infected_people, entries_exits)
print(" ".join(map(str, output)))
