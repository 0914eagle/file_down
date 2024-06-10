
def solve(n, a, b):
    pos = [0] * (n + 1) # pos[i] = the position of card i in the pile
    for i in range(n):
        pos[b[i]] = i
    
    empty = [] # empty = the positions of empty cards in the pile
    for i in range(n):
        if b[i] == 0:
            empty.append(i)
    
    ans = 0
    for i in range(1, n + 1):
        if a[i - 1] != 0:
            continue
        
        while pos[i] not in empty:
            ans += 1
            empty.append(pos[i])
            pos[a[empty[0]]] = pos[i]
            a[empty[0]] = i
            empty = empty[1:]
    
    return ans

