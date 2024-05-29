
def maximize_duels(n):
    board = [["" for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if (i+j) % 2 == 0:
                board[i][j] = "B"
            else:
                board[i][j] = "W"
    
    return "\n".join(["".join(row) for row in board])

# Input
n = int(input())

# Output
print(maximize_duels(n))
```
