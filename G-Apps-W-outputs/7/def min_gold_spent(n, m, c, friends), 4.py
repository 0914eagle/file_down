
def min_gold_spent(n, m, c, friends):
    total_gold = sum(c)
    visited = [False] * n
    min_gold = 0

    for i in range(n):
        if not visited[i]:
            min_cost = float('inf')
            queue = [i]
            visited[i] = True

            while queue:
                curr = queue.pop(0)
                min_cost = min(min_cost, c[curr])
                for friend in friends[curr]:
                    if not visited[friend]:
                        queue.append(friend)
                        visited[friend] = True
            
            min_gold += min_cost

    return min_gold

# Input
n, m = map(int, input().split())
c = list(map(int, input().split()))

friends = {}
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if x not in friends:
        friends[x] = []
    if y not in friends:
        friends[y] = []
    friends[x].append(y)
    friends[y].append(x)

# Output
print(min_gold_spent(n, m, c, friends))
