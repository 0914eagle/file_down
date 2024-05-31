
def min_gold_to_finish_quest(n, m, costs, friendships):
    adj_list = {i: [] for i in range(1, n+1)}
    
    for x, y in friendships:
        adj_list[x].append(y)
        adj_list[y].append(x)
    
    visited = set()
    total_gold = 0
    
    for i in range(1, n+1):
        if i not in visited:
            min_cost = float('inf')
            stack = [i]
            
            while stack:
                current = stack.pop()
                visited.add(current)
                min_cost = min(min_cost, costs[current-1])
                
                for neighbor in adj_list[current]:
                    if neighbor not in visited:
                        stack.append(neighbor)
            
            total_gold += min_cost
    
    return total_gold

# Input parsing
n, m = map(int, input().split())
costs = list(map(int, input().split()))
friendships = [tuple(map(int, input().split())) for _ in range(m)]

# Call the function and print the result
print(min_gold_to_finish_quest(n, m, costs, friendships))
