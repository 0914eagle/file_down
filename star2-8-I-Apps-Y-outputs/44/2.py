
from sys import stdin
n, k = map(int, stdin.readline().split())
ids = list(map(int, stdin.readline().split()))
conversations = {}
result = []
for id in ids:
  if id in conversations:
    result.append(id)
  else:
    conversations[id] = True
    result.append(id)
    if len(conversations) > k:
      conversations.pop(result.pop(0))
print(len(conversations))
print(*result)

