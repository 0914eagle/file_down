
import numpy as np
import math
import sys
sys.setrecursionlimit(10**5)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    cnt = np.zeros(n, dtype=np.int64)
    cnt[1:] = a[:-1]
    ans = []
    for i in range(2, n):
        ans.append((1, i))
        cnt[1] -= 1
        cnt[i] -= 1
    for i in range(2, n):
        for j in range(i + 1, n):
            if cnt[i] == 0 and cnt[j] == 0:
                break
            if cnt[i] >= 1 and cnt[j] >= 1:
                cnt[i] -= 1
                cnt[j] -= 1
                ans.append((i, j))
    if cnt[1] != 0:
        print("NO")
        return
    ans.append((1, 2))
    print("YES", max(a))
    print(len(ans))
    for i, j in ans:
        print(i, j)


if __name__ == '__main__':
    main()
