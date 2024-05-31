
def min_gold_to_finish_quest(n, m, characters, friendships):
    total_gold = 0
    friends = {}
    
    for x, y in friendships:
        if x not in friends:
            friends[x] = set()
        friends[x].add(y)
        
        if y not in friends:
            friends[y] = set()
        friends[y].add(x)
    
    visited = set()
    for i in range(1, n+1):
        if i not in visited:
            min_gold = float('inf')
            queue = [i]
            while queue:
                curr = queue.pop(0)
                visited.add(curr)
                min_gold = min(min_gold, characters[curr-1])
                if curr in friends:
                    for friend in friends[curr]:
                        if friend not in visited:
                            queue.append(friend)
            
            total_gold += min_gold
    
    return total_gold

# Input processing
n, m = map(int, input().split())
characters = list(map(int, input().split()))
friendships = [tuple(map(int, input().split())) for _ in range(m)]

# Call the function and print the result
print(min_gold_to_finish_quest(n, m, characters, friendships))
