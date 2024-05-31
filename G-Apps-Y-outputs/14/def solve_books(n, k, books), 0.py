
def solve_books(n, k, books):
    alice_books = []
    bob_books = []
    for t, a, b in books:
        if a == 1 and b == 1:
            alice_books.append(t)
            bob_books.append(t)
        elif a == 1:
            alice_books.append(t)
        elif b == 1:
            bob_books.append(t)
    
    alice_books.sort()
    bob_books.sort()

    if len(alice_books) < k or len(bob_books) < k:
        return -1

    total_time = 0
    for i in range(k):
        total_time += min(alice_books[i], bob_books[i])
    
    return total_time

# Input parsing
n, k = map(int, input().split())
books = [tuple(map(int, input().split())) for _ in range(n)]

# Call the function and print the result
result = solve_books(n, k, books)
print(result)
