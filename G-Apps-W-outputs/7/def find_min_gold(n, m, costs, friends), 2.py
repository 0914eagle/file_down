
def find_min_gold(n, m, costs, friends):
    total_cost = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            cost = float('inf')
            stack = [i]
            visited[i] = True
            while stack:
                curr = stack.pop()
                cost = min(cost, costs[curr])
                for friend in friends[curr]:
                    if not visited[friend]:
                        stack.append(friend)
                        visited[friend] = True
            total_cost += cost
    return total_cost

# Input parsing
n, m = map(int, input().split())
costs = list(map(int, input().split()))
friends = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    friends[x-1].append(y-1)
    friends[y-1].append(x-1)

# Call the function and print the result
result = find_min_gold(n, m, costs, friends)
print(result)
