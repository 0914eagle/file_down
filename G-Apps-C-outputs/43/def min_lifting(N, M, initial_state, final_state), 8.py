
def min_lifting(N, M, initial_state, final_state):
    def count_books(state):
        books = set()
        for shelf in state:
            for book in shelf:
                if book != 0:
                    books.add(book)
        return len(books)

    def find_book_pos(state, book):
        for i, shelf in enumerate(state):
            if book in shelf:
                return (i, shelf.index(book))
        return None

    def move_book(state, from_pos, to_pos):
        from_i, from_j = from_pos
        to_i, to_j = to_pos
        book = state[from_i][from_j]
        state[from_i][from_j] = 0
        state[to_i][to_j] = book

    def count_lifting(initial_state, final_state):
        moves = 0
        while count_books(initial_state) > 0:
            for book in range(1, count_books(initial_state) + 1):
                initial_pos = find_book_pos(initial_state, book)
                final_pos = find_book_pos(final_state, book)
                if initial_pos != final_pos:
                    lift_one = abs(initial_pos[0] - final_pos[0])
                    lift_two = abs(initial_pos[1] - final_pos[1])
                    moves += lift_one + lift_two
                    move_book(initial_state, initial_pos, final_pos)
        return moves

    return count_lifting(initial_state, final_state)

# Reading input
N, M = map(int, input().split())
initial_state = [list(map(int, input().split())) for _ in range(N)]
final_state = [list(map(int, input().split())) for _ in range(N)]

min_lifts = min_lifting(N, M, initial_state, final_state)
print(min_lifts if min_lifts >= 0 else -1)
