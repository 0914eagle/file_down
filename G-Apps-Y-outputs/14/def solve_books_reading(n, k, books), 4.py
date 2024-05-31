
def solve_books_reading(n, k, books):
    alice_likes = []
    bob_likes = []
    both_like = []
    for i in range(n):
        t, a, b = books[i]
        if a == 1 and b == 1:
            both_like.append(t)
        elif a == 1:
            alice_likes.append(t)
        elif b == 1:
            bob_likes.append(t)
    
    alice_likes.sort()
    bob_likes.sort()
    both_like.sort()
    
    if len(both_like) < k:
        return -1
    
    total_time = sum(both_like[:k])
    
    remaining_a = max(0, k - len(both_like))
    remaining_b = max(0, k - len(both_like))
    
    for i in range(remaining_a):
        if i < len(alice_likes) and i < len(bob_likes):
            total_time += alice_likes[i] + bob_likes[i]
        else:
            return -1
    
    return total_time

# Input processing
n, k = map(int, input().split())
books = []
for _ in range(n):
    t, a, b = map(int, input().split())
    books.append((t, a, b))

# Solve the problem
result = solve_books_reading(n, k, books)
print(result)
