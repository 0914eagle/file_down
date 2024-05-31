
def min_reading_time(n, k, books):
    alice_books = []
    bob_books = []
    common_books = []
    
    for i in range(n):
        if books[i][1] == 1 and books[i][2] == 1:
            common_books.append(books[i][0])
        elif books[i][1] == 1:
            alice_books.append(books[i][0])
        elif books[i][2] == 1:
            bob_books.append(books[i][0])
    
    alice_books.sort(reverse=True)
    bob_books.sort(reverse=True)
    
    min_time = float('inf')
    
    for i in range(min(k, min(len(alice_books), len(bob_books)))+1):
        if i <= len(alice_books) and k-i <= len(bob_books):
            time = sum(alice_books[:i]) + sum(bob_books[:k-i]) + sum(common_books)
            min_time = min(min_time, time)
    
    return min_time if min_time != float('inf') else -1

# Input reading and function call
n, k = map(int, input().split())
books = [list(map(int, input().split())) for _ in range(n)]
print(min_reading_time(n, k, books))
