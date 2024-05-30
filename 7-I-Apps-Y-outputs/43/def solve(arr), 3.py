
import sys

def solve(arr):
    n = len(arr)
    count = 0
    for i in range(1, n + 1):
        flag = True
        for j in range(1, i):
            if arr[i - 1] < arr[j - 1]:
                flag = False
                break
        if flag:
            count += 1
    return count

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    print(solve(arr))

