
def minimal_number_of_lifting(N, M, current_state, wanted_state):
    def count_lifting(shelf1, shelf2):
        lifting = 0
        for i in range(M):
            if shelf1[i] != shelf2[i]:
                lifting += 1
        return lifting

    def find_book_position(state, book):
        for i in range(N):
            if book in state[i]:
                return i, state[i].index(book)
        return -1, -1

    current_books = []
    wanted_books = []
    for i in range(N):
        current_books.extend(current_state[i])
        wanted_books.extend(wanted_state[i])

    if set(current_books) != set(wanted_books):
        return -1

    lifting = 0
    for book in wanted_books:
        current_row, current_col = find_book_position(current_state, book)
        wanted_row, wanted_col = find_book_position(wanted_state, book)
        if current_row != wanted_row:
            lifting += 1
        elif current_col != wanted_col:
            lifting += abs(current_col - wanted_col)

    return lifting

# Input parsing
N, M = map(int, input().split())
current_state = [list(map(int, input().split())) for _ in range(N)]
wanted_state = [list(map(int, input().split())) for _ in range(N)]

# Output
print(minimal_number_of_lifting(N, M, current_state, wanted_state))
