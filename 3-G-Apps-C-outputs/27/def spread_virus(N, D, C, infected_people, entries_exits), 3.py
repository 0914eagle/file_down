
def spread_virus(N, D, C, infected_people, entries_exits):
    infected = set(infected_people)
    contacts = [set() for _ in range(D+1)]

    for i in range(N):
        s_i, t_i = entries_exits[i]
        for j in range(1, D+1):
            if s_i <= j and j <= t_i:
                contacts[j].add(i+1)

    for day in range(1, D+1):
        new_infected = set()
        for person in contacts[day]:
            if person in infected:
                new_infected.update(contacts[day])
        infected.update(new_infected)

    return sorted(infected)

# Read input
N, D = map(int, input().split())
C, *infected_people = map(int, input().split())
entries_exits = [list(map(int, input().split())) for _ in range(N)]

# Call the function and print the result
result = spread_virus(N, D, C, infected_people, entries_exits)
print(' '.join(map(str, result)))
