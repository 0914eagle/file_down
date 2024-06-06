
a = int(input())
b = int(input())
a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))

res = []
for i in a_arr:
    for j in b_arr:
        res.append(i*j)

res.sort()
print(res[0])
