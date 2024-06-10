
n, m = map(int, input().split())
chests = list(map(int, input().split()))
keys = list(map(int, input().split()))

def solve(n, m, chests, keys):
    odd_chests = [a for a in chests if a % 2 == 1]
    odd_keys = [b for b in keys if b % 2 == 1]
    even_chests = [a for a in chests if a % 2 == 0]
    even_keys = [b for b in keys if b % 2 == 0]
    
    odd_keys.sort()
    odd_chests.sort()
    
    even_keys.sort()
    even_chests.sort()
    
    res = 0
    
    for key in odd_keys:
        if len(odd_chests) == 0:
            break
        
        chest = odd_chests.pop()
        
        if chest + key % 2 == 1:
            res += 1
    
    for key in even_keys:
        if len(even_chests) == 0:
            break
        
        chest = even_chests.pop()
        
        if chest + key % 2 == 1:
            res += 1
    
    return res

print(solve(n, m, chests, keys))

