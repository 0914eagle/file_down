
n, k = map(int, input().split())
ids = list(map(int, input().split()))
conversations = set()
result = []
for i in range(n):
    if ids[i] in conversations:
        continue
    if len(conversations) == k:
        conversations.remove(result[-1])
    conversations.add(ids[i])
    result.append(ids[i])
print(len(conversations))
print(*result)

