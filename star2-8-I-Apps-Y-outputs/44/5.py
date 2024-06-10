
n, k = map(int, input().split())
ids = list(map(int, input().split()))
conversations = []
for id in ids:
    if id in conversations:
        conversations.remove(id)
    else:
        if len(conversations) == k:
            conversations.pop()
    conversations.insert(0, id)
print(len(conversations))
print(*conversations)

