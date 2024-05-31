
def min_gold_spent(n, m, c, friendships):
    friends = {}
    for x, y in friendships:
        if x not in friends:
            friends[x] = set()
        if y not in friends:
            friends[y] = set()
        friends[x].add(y)
        friends[y].add(x)

    total_gold_spent = 0
    visited = [False] * (n + 1)

    for i in range(1, n + 1):
        if not visited[i]:
            min_gold = float('inf')
            stack = [i]
            while stack:
                current = stack.pop()
                visited[current] = True
                min_gold = min(min_gold, c[current - 1])
                if current in friends:
                    for friend in friends[current]:
                        if not visited[friend]:
                            stack.append(friend)
            total_gold_spent += min_gold

    return total_gold_spent

# Read input
n, m = map(int, input().split())
c = list(map(int, input().split()))
friendships = [tuple(map(int, input().split())) for _ in range(m)]

# Call the function and print the result
print(min_gold_spent(n, m, c, friendships))
