
def solve_books(n, k, books):
    alice_books = []
    bob_books = []
    both_books = []
    
    for i in range(n):
        t, a, b = books[i]
        if a == 1 and b == 1:
            both_books.append((t, i))
        elif a == 1:
            alice_books.append((t, i))
        elif b == 1:
            bob_books.append((t, i))
    
    alice_books.sort()
    bob_books.sort()
    both_books.sort()
    
    if len(both_books) < k:
        return -1
    
    total_time = sum([t for t, _ in both_books[:k]])
    
    for i in range(k, min(len(both_books), len(alice_books), len(bob_books)) + 1):
        total_time = min(total_time, sum([t for t, _ in both_books[:i]]) +
                        sum([t for t, _ in alice_books[:k-(i-k)]] +
                        sum([t for t, _ in bob_books[:k-(i-k)]]))
    
    if total_time == float('inf'):
        return -1
    else:
        return total_time

# Input parsing
n, k = map(int, input().split())
books = [list(map(int, input().split())) for _ in range(n)]

result = solve_books(n, k, books)
print(result)
