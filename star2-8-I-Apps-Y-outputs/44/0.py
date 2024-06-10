
n, k = map(int, input().split())
ids = list(map(int, input().split()))
conversations = set()
output = []
for i in range(n):
    if ids[i] in conversations:
        continue
    if len(conversations) == k:
        conversations.remove(output[-1])
    output.append(ids[i])
    conversations.add(ids[i])
print(len(output))
print(*output)

