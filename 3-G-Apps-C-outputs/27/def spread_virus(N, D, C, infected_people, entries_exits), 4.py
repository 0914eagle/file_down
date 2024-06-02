
def spread_virus(N, D, C, infected_people, entries_exits):
    infected = set(infected_people)
    contacts = [set() for _ in range(D+1)]
    
    for i in range(N):
        for j in range(i+1, N):
            if entries_exits[i][1] >= entries_exits[j][0] and entries_exits[i][0] <= entries_exits[j][1]:
                contacts[0].add((i+1, j+1))
    
    for day in range(1, D+1):
        for contact in contacts[day-1]:
            for i in range(N):
                if i+1 not in infected and (i+1, contact[0]) in contacts[0] and (i+1, contact[1]) in contacts[0]:
                    infected.add(i+1)
                    contacts[day].add((i+1, contact[0]))
                    contacts[day].add((i+1, contact[1))
    
    return sorted(infected)

# Input parsing
N, D = map(int, input().split())
C, *infected_people = map(int, input().split())
entries_exits = [list(map(int, input().split())) for _ in range(N)]

result = spread_virus(N, D, C, infected_people, entries_exits)
print(' '.join(map(str, result)))
