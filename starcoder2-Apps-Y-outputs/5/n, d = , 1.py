
n, d = map(int, input().split())
d_m = int(input())
d_list = list(map(int, input().split()))

for i in range(n):
    if d_list[i] > d_m:
        print("It hadn't snowed this early in", i, "years!")
        break
else:
    print("It had never snowed this early!")

