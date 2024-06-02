
def spread_virus(N, D, C, infected, entries):
    room = set()
    infected_set = set(infected)
    for day in range(D):
        new_infected = set()
        for i in range(N):
            if i + 1 not in infected_set:
                if entries[i][0] <= day and entries[i][1] >= day:
                    room.add(i + 1)
                if entries[i][0] == day and entries[i][1] == day:
                    room.add(i + 1)
            if i + 1 in infected_set:
                new_infected.update(room)
        infected_set.update(new_infected)
    
    return ' '.join(map(str, sorted(infected_set)))

# Input parsing
N, D = map(int, input().split())
C, *infected = map(int, input().split())
entries = [tuple(map(int, input().split())) for _ in range(N)]

# Call the function and print the result
print(spread_virus(N, D, C, infected, entries))
