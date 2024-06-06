
# 123456 14323 1700000
# 123458 41412 1900000
# 123457 15221 1800000

# 123456
# 123458
# 123457

# 123457 0
# 0 2
# 123458 1

n, q = map(int, input().split())

dic = dict()

for _ in range(n):
    k, s, h = map(int, input().split())
    dic[k] = (s, h)

chairperson = sorted(dic.items(), key=lambda x: (x[1][0], -x[1][1]))[0][0]

def query(k, chairperson):
    if k == chairperson:
        return '0 2'
    else:
        boss = sorted(dic.items(), key=lambda x: (x[1][0], -x[1][1]), reverse=True)
        for i in range(n):
            if boss[i][0] != k and boss[i][1][1] <= dic[k][1]:
                subordinates = sorted(dic.items(), key=lambda x: (x[1][0], -x[1][1]))
                sub = 0
                for j in range(n):
                    if subordinates[j][1][0] > dic[k][0] and subordinates[j][1][1] >= dic[k][1] and boss[i][0] == subordinates[j][0]:
                        sub += 1
                return f'{boss[i][0]} {sub}'
            
for _ in range(q):
    k = int(input())
    print(query(k, chairperson))
