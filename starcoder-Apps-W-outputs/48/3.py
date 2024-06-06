
v = int(input())
a = [int(x) for x in input().split()]
sum1 = 0
arr = [i for i in range(1,10)]
brr = sorted(a)
for i in range(9):
    sum1 += brr[i]
    if sum1 > v:
        for j in range(8,-1,-1):
            if brr[j] + sum1 - brr[i] <= v:
                brr[i] = brr[j]
                break
        break
if sum1 > v:
    print(-1)
else:
    for i in range(9):
        if brr[i] != a[i]:
            arr[i] = 0
    if arr[0] == 0:
        print(-1)
    else:
        arr = ''.join([str(x) for x in arr])
        print(arr)
