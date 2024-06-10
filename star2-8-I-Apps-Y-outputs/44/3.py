
n, k = map(int, input().split())
ids = list(map(int, input().split()))
conv = dict()
displayed = []
for id in ids:
    if id in conv:
        conv[id] += 1
    else:
        conv[id] = 1
        if len(displayed) == k:
            del conv[displayed.pop()]
        displayed.insert(0, id)
print(len(displayed))
print(*displayed)

