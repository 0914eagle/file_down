
def min_lifting(N, M, initial_state, final_state):
    def find_position(book, state):
        for i, shelf in enumerate(state):
            if book in shelf:
                return i, shelf.index(book)
        return None, None

    def count_lifting(initial_state, final_state):
        moves = 0
        for book in range(1, len(initial_state) + 1):
            init_i, init_j = find_position(book, initial_state)
            final_i, final_j = find_position(book, final_state)
            if init_i is None or final_i is None:
                return -1
            moves += abs(init_i - final_i) + abs(init_j - final_j)
        return moves

    return count_lifting(initial_state, final_state)

# Input parsing
N, M = map(int, input().split())
initial_state = [list(map(int, input().split())) for _ in range(N)]
final_state = [list(map(int, input().split())) for _ in range(N)]

# Calculate and print the minimal number of lifting needed
result = min_lifting(N, M, initial_state, final_state)
print(result)
