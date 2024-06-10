
n = int(input())
a = [int(i) for i in input().split()]
maxa = max(a)

for k in range(2, maxa+1):
    if all(i%k==0 for i in a):
        break
else:
    print(-1)
    exit()

res = 0
for i in a:
    res += i//k * k - i

print(res)


