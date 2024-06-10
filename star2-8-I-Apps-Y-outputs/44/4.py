
n, k = map(int, input().split())
ids = list(map(int, input().split()))
conversations = []
for i in range(n):
  if ids[i] in conversations:
    conversations.remove(ids[i])
  else:
    if len(conversations) == k:
      conversations.pop()
  conversations.insert(0, ids[i])
print(len(conversations))
print(' '.join(map(str, conversations)))

