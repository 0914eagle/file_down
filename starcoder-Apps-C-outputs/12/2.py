

n = int(input())

s = input()

grid = []

for i in range(n):
    grid.append(input())

# This algorithm is based on the finite automaton theory

# where in, each state is considered as the last

# two characters of the trail and where,

# transitions are performed according to the

# program of the robot

# If a state is visited for the second time,

# it means that the robot will keep moving and

# will eventually loop back and make the trail

# of robot infinite

# For each state, we'll calculate the prefix

# it generates and calculate the frequency

# of occurence of each of its prefixes

states = []

visited = {}

prefixes = {}

for i in range(n):

    for j in range(n):

        if grid[i][j] == 'R':

            row = i

            col = j

for i in range(len(s)):

    if s[i] == '<':

        col -= 1

    elif s[i] == '>':

        col += 1

    elif s[i] == '^':

        row -= 1

    elif s[i] == 'v':

        row += 1

    state = (row, col)

    if state in visited:

        print(visited[state])

        break

    states.append(state)

    visited[state] = i + 1

    prefix = ''.join([grid[states[i][0]][states[i][1]] for i in range(len(states))])

    if prefix in prefixes:

        prefixes[prefix] += 1

    else:

        prefixes[prefix] = 1

else:

    print(len(prefix))

