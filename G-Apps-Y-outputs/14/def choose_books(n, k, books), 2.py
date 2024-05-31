
def choose_books(n, k, books):
    alice_books = []
    bob_books = []
    shared_books = []

    for i in range(n):
        ti, ai, bi = books[i]
        if ai == 1 and bi == 1:
            shared_books.append((ti, ai, bi))
        elif ai == 1:
            alice_books.append((ti, ai, bi))
        elif bi == 1:
            bob_books.append((ti, ai, bi))

    alice_books.sort()
    bob_books.sort()
    shared_books.sort()

    if len(shared_books) < k:
        return -1

    total_time = 0
    while len(shared_books) < k and (alice_books or bob_books):
        if alice_books and bob_books:
            if alice_books[0][0] < bob_books[0][0]:
                total_time += alice_books[0][0]
                alice_books.pop(0)
            else:
                total_time += bob_books[0][0]
                bob_books.pop(0)
        elif alice_books:
            total_time += alice_books[0][0]
            alice_books.pop(0)
        elif bob_books:
            total_time += bob_books[0][0]
            bob_books.pop(0)
    
    for t, _, _ in shared_books:
        total_time += t
    
    return total_time

# Read input
n, k = map(int, input().split())
books = [list(map(int, input().split())) for _ in range(n)]

# Call the function and print the result
print(choose_books(n, k, books))
