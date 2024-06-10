
n, k = map(int, input().split())
conversations = []
last_seen = {}
for idx, friend_id in enumerate(map(int, input().split())):
    if friend_id in last_seen:
        conversations.remove(friend_id)
    else:
        if len(conversations) == k:
            conversations.pop()
    conversations.insert(0, friend_id)
    last_seen[friend_id] = idx
print(len(conversations))
print(*conversations)

