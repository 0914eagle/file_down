
def min_lifting(N, M, initial, final):
    books = {}
    for i in range(N):
        for j in range(M):
            if initial[i][j] != 0:
                books[initial[i][j]] = (i, j)
    
    moves = 0
    for i in range(N):
        for j in range(M):
            if final[i][j] != 0 and final[i][j] != initial[i][j]:
                book_num = final[i][j]
                target_i, target_j = books[book_num]
                
                diff_i = abs(i - target_i)
                diff_j = abs(j - target_j)
                
                moves += min(diff_i, N - diff_i) + min(diff_j, M - diff_j)
                
                # update the book's position
                books[book_num] = (i, j)
    
    return moves

# Read input
N, M = map(int, input().split())
initial = []
for _ in range(N):
    initial.append(list(map(int, input().split())))
final = []
for _ in range(N):
    final.append(list(map(int, input().split())))

result = min_lifting(N, M, initial, final)
print(result)
