

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    swap_list = []
    for i in range(n):
        idx = arr.index(min(arr[i:]))
        if idx != i:
            swap_list.append((i, idx))
            arr[i], arr[idx] = arr[idx], arr[i]
    
    print(len(swap_list))
    for i, j in swap_list:
        print(i, j)

solve()


