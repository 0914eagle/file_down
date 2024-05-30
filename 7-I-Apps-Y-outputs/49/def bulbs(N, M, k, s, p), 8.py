
def bulbs(N, M, k, s, p):
    # Write your code here
    res = 0
    for i in range(2**N):
        count = 0
        for j in range(M):
            if i & (1 << j) and s[j][0] <= N:
                for kk in range(s[j][0], s[j][0] + s[j][1]):
                    if kk <= N and (i >> kk) & 1:
                        count += 1
        if count % 2 == p[j]:
            res += 1
    return res

