
def find_min_gold_spent(n, m, gold_costs, friendships):
    friends = {}
    for x, y in friendships:
        if x not in friends:
            friends[x] = set()
        if y not in friends:
            friends[y] = set()
        friends[x].add(y)
        friends[y].add(x)
    
    visited = [False] * (n + 1)
    total_gold_spent = 0
    
    def dfs(node):
        nonlocal total_gold_spent
        visited[node] = True
        total_gold_spent += gold_costs[node - 1]
        if node in friends:
            for friend in friends[node]:
                if not visited[friend]:
                    dfs(friend)
    
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
    
    return total_gold_spent

# Input parsing
n, m = map(int, input().split())
gold_costs = list(map(int, input().split()))
friendships = [tuple(map(int, input().split())) for _ in range(m)]

# Find minimum amount of gold Vova needs to spend
result = find_min_gold_spent(n, m, gold_costs, friendships)
print(result)
