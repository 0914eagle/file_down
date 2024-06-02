
def spread_virus(N, D, C, infected_people, entries_exits):
    infected = set(infected_people)
    contacts = [set() for _ in range(D+1)]
    
    for day in range(1, D+1):
        for i in range(N):
            if i+1 in infected:
                for j in range(i+1, N):
                    if entries_exits[i][1] >= entries_exits[j][0]:
                        contacts[day].add(j+1)
                    else:
                        break
        
        if day < D:
            for person in contacts[day]:
                infected.add(person)
    
    return sorted(infected)

# Input processing
N, D = map(int, input().split())
C, *infected_people = map(int, input().split())
entries_exits = [list(map(int, input().split())) for _ in range(N)]

result = spread_virus(N, D, C, infected_people, entries_exits)
print(" ".join(map(str, result)))
