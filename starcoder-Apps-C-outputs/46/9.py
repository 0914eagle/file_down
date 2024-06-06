

n,l,r = map(int, input().split())

arr = list()

arr.append(n)

while 1 not in arr:
    for i in range(len(arr)):
        if arr[i] > 1:
            arr[i] = arr[i] // 2
            arr.insert(i, arr[i])
            arr.insert(i, arr[i] % 2)
            arr.insert(i, arr[i] // 2)
            del arr[i+1]
            break

#print(arr)

print(sum(arr[l-1:r]))

