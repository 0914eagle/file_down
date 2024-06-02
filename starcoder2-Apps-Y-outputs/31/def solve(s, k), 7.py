
def solve(s, k):
    n = len(s)
    cnt = 0
    for i in range(n):
        for j in range(i, n):
            cnt += 1
            if cnt == k:
                return s[i:j+1]

s = input()
k = int(input())
print(solve(s, k))

