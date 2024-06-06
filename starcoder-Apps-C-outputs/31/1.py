
n, p = [float(i) for i in input().split()]
data = []
for i in range(int(n)):
    data.append([float(i) for i in input().split()])
data.sort(key=lambda x: x[1] / x[0])
ans = 0
prob = 1
for i in range(len(data)):
    prob *= data[i][1]
    if prob >= p:
        ans += data[i][0]
        break
    else:
        ans += data[i][0]
print(int(ans))
