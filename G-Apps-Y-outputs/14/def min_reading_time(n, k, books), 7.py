
def min_reading_time(n, k, books):
    alice_books = []
    bob_books = []
    both_books = []
    
    for t, a, b in books:
        if a == 1 and b == 1:
            both_books.append(t)
        elif a == 1:
            alice_books.append(t)
        elif b == 1:
            bob_books.append(t)
    
    alice_books.sort()
    bob_books.sort()
    both_books.sort()
    
    if len(both_books) < k:
        return -1
    
    min_time = sum(both_books[:k])
    
    for i in range(1, min(k, len(both_books)) + 1):
        if len(alice_books) >= k - i and len(bob_books) >= k - i:
            min_time = min(min_time, sum(both_books[:i]) + sum(alice_books[:k-i]) + sum(bob_books[:k-i]))
    
    return min_time

# Input reading
n, k = map(int, input().split())
books = []
for _ in range(n):
    t, a, b = map(int, input().split())
    books.append((t, a, b))

# Call the function and output the result
result = min_reading_time(n, k, books)
print(result)
