
n = int(input())
cafes = list(map(int, input().split()))
last_visit = dict()
for i, cafe in enumerate(cafes):
    last_visit[cafe] = i
min_cafe = min(last_visit, key=last_visit.get)
print(min_cafe)

