
def spread_virus(N, D, C, infected_people, entries_exits):
    infected_set = set(infected_people)
    contacts = [[] for _ in range(D+1)]
    
    for i in range(N):
        for j in range(i+1, N):
            if entries_exits[i][0] <= entries_exits[j][1] and entries_exits[j][0] <= entries_exits[i][1]:
                for day in range(1, D+1):
                    if entries_exits[i][0] == entries_exits[i][1] or entries_exits[j][0] == entries_exits[j][1]:
                        contacts[day].append((i+1, j+1))
                    elif entries_exits[i][0] < entries_exits[j][1] and entries_exits[j][0] < entries_exits[i][1]:
                        contacts[day].append((i+1, j+1))
    
    for day in range(1, D+1):
        new_infected = set()
        for person1, person2 in contacts[day]:
            if person1 in infected_set and person2 not in infected_set:
                new_infected.add(person2)
            elif person2 in infected_set and person1 not in infected_set:
                new_infected.add(person1)
        infected_set.update(new_infected)
    
    return sorted(list(infected_set))

# Input parsing
N, D = map(int, input().split())
C, *infected_people = map(int, input().split())
entries_exits = [list(map(int, input().split())) for _ in range(N)]

result = spread_virus(N, D, C, infected_people, entries_exits)
print(' '.join(map(str, result)))
