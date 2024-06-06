
# 1. 读入公司数量
C = int(input())
# 2. 读入每家公司的股票数量
for i in range(C):
    # 2.1 读入每家公司的股票数量
    K = int(input())
    # 2.2 读入每家公司的股票数量
    for j in range(K):
        # 2.2.1 读入每家公司的股票数量
        N, D = map(int, input().split())
        # 2.2.2 读入每家公司的股票数量
        if D in days:
            days[D] += N
        else:
            days[D] = N
# 3. 输出每天的股票数量
for i in sorted(days):
    print(days[i], end=' ')
