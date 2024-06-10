
k = int(input())
num = 9
count = 0
while count < k:
    if sum(map(int, str(num))) == 10:
        count += 1
    num += 1
print(num - 1)

