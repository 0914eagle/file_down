
def spread_virus(N, D, C, infected_people, entries_exits):
    infected = set(infected_people)
    contacts = {day: set() for day in range(D + 1)}
    
    for day in range(1, D + 1):
        for i in range(N):
            if i + 1 not in infected:
                for j in range(i + 1):
                    if j + 1 in infected and entries_exits[i][0] <= entries_exits[j][1] and entries_exits[j][0] <= entries_exits[i][1]:
                        contacts[day].add(i + 1)
                        break
    
    for day in range(1, D + 1):
        for person in contacts[day]:
            infected.add(person)
    
    return sorted(infected)

# Input parsing
N, D = map(int, input().split())
C, *infected_people = map(int, input().split())
entries_exits = [list(map(int, input().split())) for _ in range(N)]

result = spread_virus(N, D, C, infected_people, entries_exits)
print(" ".join(map(str, result)))
