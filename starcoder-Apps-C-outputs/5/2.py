
n = int(input())
array = list(map(int,input().split()))

if len(array) == 1:
    print(array[0])
    exit()

array.sort()

count = 0
for i in range(len(array)):
    if i == 0:
        count += array[i]
    elif i == len(array) - 1:
        count += array[i]
    else:
        if array[i] > array[i-1]:
            if array[i] > array[i+1]:
                count += array[i]
print(count)
