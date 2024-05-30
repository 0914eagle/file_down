
def is_good_matrix(a):
    n, m = len(a), len(a[0])
    
    ans = 0
    
    for i in range(n):
        for j in range(m):
            ones = 0
            zeros = 0
            for k in range(i, n):
                for l in range(j, m):
                    if a[k][l] == '1':
                        ones += 1
                    else:
                        zeros += 1
                    if (k - i + 1) % 2 == 0 and (l - j + 1) % 2 == 0:
                        if ones % 2 == 0:
                            ans += 1
                        if zeros % 2 == 0:
                            ans += 1
    return ans

n, m = map(int, input().split())
a = [input() for _ in range(n)]

result = is_good_matrix(a)

if result % 2 == 1:
    print(result // 2)
else:
    print(-1)
```
