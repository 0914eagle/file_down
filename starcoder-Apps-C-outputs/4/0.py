
N = int(input())
index = [0] * 2001

for i in range(2*N):
    c, a = input().split()
    if c == "W":
        index[int(a)] = i+1

# print(index)

i = 1
cnt = 0
while i <= N:
    if index[i] != i:
        index[0], index[i] = index[i], index[0]
        cnt += 1
    i += 1
# print(index)

i = 1
while i < N:
    if index[i] > index[i+1]:
        index[i], index[i+1] = index[i+1], index[i]
        cnt += 1
    i += 1
# print(index)

i = 1
while i <= N:
    if index[i] != i:
        index[0], index[i] = index[i], index[0]
        cnt += 1
    i += 1

print(cnt)
