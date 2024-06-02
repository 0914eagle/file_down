
def get_infected_people(N, D, C, infected_people, entries_exits):
    contacts = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            if entries_exits[i][0] <= entries_exits[j][1] and entries_exits[j][0] <= entries_exits[i][1]:
                contacts[i].append(j)
                contacts[j].append(i)

    infected = set(infected_people)
    for _ in range(D):
        new_infected = set()
        for person in infected:
            for contact in contacts[person]:
                if contact not in infected:
                    new_infected.add(contact)
        infected.update(new_infected)

    return sorted(list(infected))


# Input processing
N, D = map(int, input().split())
C, *infected_people = map(int, input().split())
entries_exits = [list(map(int, input().split())) for _ in range(N)]

result = get_infected_people(N, D, C, infected_people, entries_exits)
print(" ".join(map(str, result)))
