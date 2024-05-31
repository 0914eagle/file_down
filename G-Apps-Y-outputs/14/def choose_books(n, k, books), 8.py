
def choose_books(n, k, books):
    alice_books = []
    bob_books = []
    
    for i in range(n):
        t, a, b = books[i]
        if a == 1 and b == 1:
            alice_books.append((t, i))
            bob_books.append((t, i))
        elif a == 1:
            alice_books.append((t, i))
        elif b == 1:
            bob_books.append((t, i))
    
    alice_books.sort()
    bob_books.sort()
    
    if len(alice_books) < k or len(bob_books) < k:
        return -1
    
    total_time = 0
    common_books = set()
    
    for i in range(k):
        total_time += alice_books[i][0]
        common_books.add(alice_books[i][1])
    
    for i in range(k):
        if bob_books[i][1] not in common_books:
            total_time += bob_books[i][0]
    
    return total_time

# Input parsing
n, k = map(int, input().split())
books = []
for _ in range(n):
    t, a, b = map(int, input().split())
    books.append((t, a, b))

result = choose_books(n, k, books)
print(result)
