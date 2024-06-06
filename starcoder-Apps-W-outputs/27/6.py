
from sys import stdin
n = int(stdin.readline().strip())
names = [stdin.readline().strip() for i in range(n)]
names.sort()
k = [0]*26
for i in range(n-1):
    l = min(len(names[i]), len(names[i+1]))
    for j in range(l):
        if names[i][j] != names[i+1][j]:
            k[ord(names[i][j])-97] += 1
            break
s = ""
for i in range(26):
    if k[i] == 0:
        s += chr(i+97)
print(s)
