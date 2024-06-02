
n, d = map(int, input().split())
d_m = int(input())
d_list = list(map(int, input().split()))

k = 0
for i in range(n):
    if d_list[i] <= d_m:
        k = i
        break

if k == 0:
    print("It had never snowed this early!")
else:
    print("It hadn't snowed this early in {} years!".format(k))

