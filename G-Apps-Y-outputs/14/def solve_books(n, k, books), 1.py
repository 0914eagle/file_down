
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
    
    if len(alice_books) < k or len(bob_books) < k:
        return -1
    
    alice_books.sort()
    bob_books.sort()
    
    total_time = sum(sorted(alice_books[:k]) + sorted(bob_books[:k]))
    
    return total_time

# Input parsing
n, k = map(int, input().split())
books = []
for _ in range(n):
    t, a, b = map(int, input().split())
    books.append((t, a, b))

# Call the function and print the output
result = solve_books(n, k, books)
print(result)
