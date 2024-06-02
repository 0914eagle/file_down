
n, d = map(int, input().split())
d_m = int(input())
d_list = list(map(int, input().split()))

d_list.reverse()
d_list.append(d_m)

k = 0
for i in range(n):
    if d_list[i] <= d_list[i+1]:
        k += 1
    else:
        break

if k == n:
    print("It had never snowed this early!")
else:
    print("It hadn't snowed this early in", k, "years!")

