
def min_gold_to_finish_quest(n, m, characters, friendships):
    parent = [i for i in range(n)]
    gold_needed = [0] * n
    
    for i in range(n):
        gold_needed[i] = characters[i]
    
    def find(x):
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        x_root = find(x)
        y_root = find(y)
        
        if x_root != y_root:
            parent[x_root] = y_root
            gold_needed[y_root] = min(gold_needed[x_root], gold_needed[y_root])
    
    for x, y in friendships:
        union(x-1, y-1)
    
    total_gold = sum(gold_needed[i] for i in range(n))
    
    return total_gold

# Input
n, m = map(int, input().split())
characters = list(map(int, input().split()))
friendships = []
for _ in range(m):
    x, y = map(int, input().split())
    friendships.append((x, y))

# Output
print(min_gold_to_finish_quest(n, m, characters, friendships))
