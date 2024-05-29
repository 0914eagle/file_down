
def maximize_duels(n):
    board = [['W' if (i+j) % 2 == 0 else 'B' for j in range(n)] for i in range(n)]
    for row in board:
        print(''.join(row))

n = int(input())
maximize_duels(n)
```
