
import sys

def solve(n, arr):
    count = 0
    for i in range(1, n+1):
        flag = True
        for j in range(1, i+1):
            if arr[i-1] < arr[j-1]:
                flag = False
                break
        if flag:
            count += 1
    return count

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(n, arr))

