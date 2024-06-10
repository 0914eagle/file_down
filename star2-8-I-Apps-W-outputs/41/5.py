
n = int(input())
cafes = list(map(int, input().split()))
last_visit = [0]*(2*10**5+1) #index of the cafe is the index of the list
for i in range(n):
    last_visit[cafes[i]] = i #update the last visit index
max_last_visit = max(last_visit)
ans = last_visit.index(max_last_visit)
print(ans)

