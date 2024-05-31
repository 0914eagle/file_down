
def destroy_tanks(n):
    if n == 2:
        return [3, [2, 1, 2]]
    
    bombs = [2, 1, 3]
    for i in range(4, n+1):
        bombs.append(i)
        bombs.append(i-1)
    
    return [len(bombs), bombs]

# Input
n = 3
result = destroy_tanks(n)

# Output
print(result[0])
print(' '.join(str(b) for b in result[1]))
