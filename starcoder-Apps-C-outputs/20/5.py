
n = int(input())
N = [input() for i in range(n)]
maxlen = 1
for i in range(n):
    for j in range(i+1, n):
        if N[i][0] == N[j][0] and N[i][-1] == N[j][-1]:
            maxlen += 1
print(maxlen)
