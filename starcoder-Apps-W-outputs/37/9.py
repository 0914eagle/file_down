
p, x = map(int, input().split())

flag = True

for i in range(1, 10):
    if i * x % 10 ** p == i:
        print(str(i) * (p - 1))
        flag = False
        break
if flag:
    print("Impossible")
