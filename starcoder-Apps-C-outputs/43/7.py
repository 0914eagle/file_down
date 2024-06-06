
n = input()
x = len(n)
flag = 0

for i in range(x):
    for j in range(x):
        if (int(n[i]) + int(n[j])) % 7 == 0 and (i != j):
            n = n[:i] + n[i + 1:]
            n = n[:j] + n[j + 1:]
            flag = 1
            break
    if flag == 1:
        break

if flag == 0:
    print('0')
else:
    print(n)
