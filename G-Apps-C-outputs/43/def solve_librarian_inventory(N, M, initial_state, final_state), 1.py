
def solve_librarian_inventory(N, M, initial_state, final_state):
    def find_book_position(state, book):
        for i in range(N):
            for j in range(M):
                if state[i][j] == book:
                    return i, j

    def manhattan_distance(book_pos, shelf_pos):
        return abs(book_pos[0] - shelf_pos[0]) + abs(book_pos[1] - shelf_pos[1])

    def move_book(book, initial_state, final_state):
        initial_pos = find_book_position(initial_state, book)
        final_pos = find_book_position(final_state, book)
        return manhattan_distance(initial_pos, final_pos)

    total_movements = 0
    for book in range(1, N*M+1):
        total_movements += move_book(book, initial_state, final_state)

    return total_movements

# Read input
N, M = map(int, input().split())
initial_state = [list(map(int, input().split())) for _ in range(N)]
final_state = [list(map(int, input().split())) for _ in range(N)]

result = solve_librarian_inventory(N, M, initial_state, final_state)
print(result)
