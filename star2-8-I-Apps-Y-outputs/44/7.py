
n, k = map(int, input().split())
ids = list(map(int, input().split()))
conversations = dict()
result = []
for i, id in enumerate(ids):
    if id in conversations:
        conversations[id] = i
    else:
        if len(conversations) == k:
            conversations = {k: v for k, v in sorted(conversations.items(), key=lambda item: item[1])}
            conversations.pop(list(conversations.keys())[-1])
        conversations[id] = i
        result.append(id)

print(len(result))
print(*result)

