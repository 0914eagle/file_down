
n = int(input())
arr = list(map(int, input().split()))
last_visit = dict()
for idx, val in enumerate(arr):
    last_visit[val] = idx
res = sorted(last_visit.items(), key=lambda x: x[1], reverse=True)[0][0]
print(res)

