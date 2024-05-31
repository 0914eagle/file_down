
def minimal_number_of_lifting(N, M, initial_state, final_state):
    books_positions = {}
    for shelf in initial_state:
        for book in shelf:
            if book != 0:
                books_positions[book] = (initial_state.index(shelf), shelf.index(book))
    
    moves = 0
    for shelf_index in range(N):
        for book_index in range(M):
            if final_state[shelf_index][book_index] != 0:
                book = final_state[shelf_index][book_index]
                if books_positions[book] != (shelf_index, book_index):
                    moves += 1
                    books_positions[book] = (shelf_index, book_index)

    return moves if moves % 2 == 0 else -1

# Input reading
N, M = map(int, input().split())
initial_state = [list(map(int, input().split())) for _ in range(N)]
final_state = [list(map(int, input().split())) for _ in range(N)]

# Output
print(minimal_number_of_lifting(N, M, initial_state, final_state))
