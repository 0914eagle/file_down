
def min_gold_spent(n, m, characters, friendships):
    friends = {}
    for x, y in friendships:
        if x not in friends:
            friends[x] = []
        if y not in friends:
            friends[y] = []
        friends[x].append(y)
        friends[y].append(x)

    visited = [False] * (n + 1)
    gold_needed = 0

    for i in range(1, n + 1):
        if not visited[i]:
            min_gold = float('inf')
            queue = [i]

            while queue:
                curr = queue.pop(0)
                visited[curr] = True
                min_gold = min(min_gold, characters[curr - 1])

                if curr in friends:
                    for friend in friends[curr]:
                        if not visited[friend]:
                            queue.append(friend)

            gold_needed += min_gold

    return gold_needed

# Input parsing
n, m = map(int, input().split())
characters = list(map(int, input().split()))
friendships = [tuple(map(int, input().split())) for _ in range(m)]

result = min_gold_spent(n, m, characters, friendships)
print(result)
