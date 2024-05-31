
def min_reading_time(n, k, books):
    likes_both = []
    likes_alice = []
    likes_bob = []

    for i in range(n):
        if books[i][1] == 1 and books[i][2] == 1:
            likes_both.append(books[i][0])
        elif books[i][1] == 1:
            likes_alice.append(books[i][0])
        elif books[i][2] == 1:
            likes_bob.append(books[i][0])

    likes_both.sort()
    likes_alice.sort()
    likes_bob.sort()

    if len(likes_both) < k:
        k -= len(likes_both)
        if len(likes_alice) < k or len(likes_bob) < k:
            return -1
        else:
            return sum(likes_both) + sum(likes_alice[:k]) + sum(likes_bob[:k])
    else:
        return sum(likes_both[:k])

# Input parsing
n, k = map(int, input().split())
books = [list(map(int, input().split())) for _ in range(n)]

result = min_reading_time(n, k, books)
print(result)
