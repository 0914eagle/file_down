
def minimal_lifting(N, M, initial_state, final_state):
    positions_dict = {}
    for i in range(N):
        for j in range(M):
            if final_state[i][j] > 0:
                positions_dict[final_state[i][j]] = (i, j)

    total_lifting = 0
    for i in range(N):
        for j in range(M):
            if initial_state[i][j] > 0 and initial_state[i][j] != final_state[i][j]:
                target_i, target_j = positions_dict[initial_state[i][j]]
                total_lifting += abs(target_i - i) + abs(target_j - j)

    return total_lifting if total_lifting % 2 == 0 else -1

# Input processing
N, M = map(int, input().split())
initial_state = []
final_state = []

for _ in range(N):
    initial_state.append(list(map(int, input().split())))

for _ in range(N):
    final_state.append(list(map(int, input().split())))

# Call the function and print the result
print(minimal_lifting(N, M, initial_state, final_state))
