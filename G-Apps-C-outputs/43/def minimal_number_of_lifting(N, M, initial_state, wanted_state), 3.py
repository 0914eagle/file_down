
def minimal_number_of_lifting(N, M, initial_state, wanted_state):
    initial_positions = {}
    wanted_positions = {}
    
    for i in range(N):
        for j in range(M):
            book = initial_state[i][j]
            if book != 0:
                initial_positions[book] = (i, j)
            
            book = wanted_state[i][j]
            if book != 0:
                wanted_positions[book] = (i, j)
    
    moves = 0
    for book, wanted_position in wanted_positions.items():
        if book in initial_positions:
            initial_position = initial_positions[book]
            moves += abs(wanted_position[0] - initial_position[0]) + abs(wanted_position[1] - initial_position[1])
    
    return moves // 2

# Input reading
N, M = map(int, input().split())
initial_state = []
wanted_state = []

for _ in range(N):
    initial_state.append(list(map(int, input().split())))

for _ in range(N):
    wanted_state.append(list(map(int, input().split())))

# Output
result = minimal_number_of_lifting(N, M, initial_state, wanted_state)
print(result)
