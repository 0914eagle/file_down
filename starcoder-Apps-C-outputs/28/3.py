
if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(1, k):
            if arr[i][j] == 1:
                arr[i][0] += 1
    for i in range(n):
        if arr[i][0] > (k / 2):
            print("NO")
            exit()
    print("YES")
