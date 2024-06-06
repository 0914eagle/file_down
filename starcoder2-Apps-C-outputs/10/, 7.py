
n = int(input())

dis = []
for i in range(n):
    dis.append(list(map(int, input().split())))

# 二分法
def check(mid):
    A = [0]
    B = []
    for i in range(1, n):
        if dis[A[0]][i] <= mid:
            A.append(i)
        else:
            B.append(i)
    for i in A:
        for j in B:
            if dis[i][j] > mid:
                return False
    return True

l, r = 0, 10**9
while l < r:
    mid = (l + r) // 2
    if check(mid):
        r = mid
    else:
        l = mid + 1
print(l)
