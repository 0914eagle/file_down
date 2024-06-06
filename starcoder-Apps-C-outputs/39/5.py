

n, g = list(map(int, input().split()))
array = []
for i in range(n):
    d, c = list(map(int, input().split()))
    array.append((d, c))

array.sort()

if array[0][0] > g:
    print("cancel road trip")
else:
    gas = g
    min_cost = 0
    for d, c in array:
        if gas >= d:
            min_cost += (d - gas) * c
            gas = d
        else:
            break
    print(min_cost)

