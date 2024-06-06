
n,d,m = map(int,input().split())
birds = []
for i in range(m):
    birds.append(int(input()))
birds.sort()
cnt = 0
for i in range(m):
    if(birds[i] - d <= 0):
        continue
    if(birds[i] + d >= n):
        break
    cnt += 1
print(cnt)
