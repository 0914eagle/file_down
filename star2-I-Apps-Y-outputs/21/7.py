
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def calc_sum(arr):
    arr.sort()
    res = 0
    for i in range(n):
        res += arr[i] * (i + 1) * (n - i)
    return res

print(calc_sum(a) + calc_sum(b) % 998244353)

