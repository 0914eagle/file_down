
# 183.py
import sys
sys.stdin = open('183.in', 'r')
sys.stdout = open('183.out', 'w')

n, m = map(int, input().split())

ans = [None for i in range(m)]
for i in range(n):
    l = list(map(int, input().split()))
    for j in range(m):
        if ans[j] == None:
            ans[j] = l[j+4]
        else:
            if ans[j] != l[j+4]:
                print(-1)
                exit(0)

for i in ans:
    print(i * 365, end=' ')
print()
