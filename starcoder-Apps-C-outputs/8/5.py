
n, m = map(int, input().split())
p = list(map(int, input().split()))
r = list(map(int, input().split()))
customers = [list(map(int, input().split())) for _ in range(n)]
customers.sort(key=lambda x:x[1])
for i in range(n):
    customers[i] = [customers[i][0]-1, customers[i][1], 0]

def serve():
    t, i = 0, 0
    while i < n:
        if t + p[customers[i][0]] <= customers[i][1]:
            customers[i][2] = 1
            t += p[customers[i][0]]
            i += 1
        else:
            break
    while i < n:
        if t + r[customers[i][0]] + p[customers[i][0]] <= customers[i][1]:
            customers[i][2] = 1
            t += r[customers[i][0]] + p[customers[i][0]]
            i += 1
        else:
            break

ans = 0
for i in range(m):
    serve()
    temp = 0
    for j in range(n):
        if customers[j][2] == 1:
            customers[j][2] = 0
            temp += 1
    ans = max(ans, temp)
print(ans)
