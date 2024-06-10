

n = int(input())
arr = list(map(int, input().split()))

def gcd(a, b):
    if a < b:
        a, b = b, a
    
    while b != 0:
        a, b = b, a % b
    
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_list(arr):
    res = arr[0]
    
    for i in range(1, len(arr)):
        res = lcm(res, arr[i])
    
    return res

if n == 1 and arr[0] == 0:
    print(-1)
else:
    l = lcm_list(arr)
    res = 0
    
    for a in arr:
        if a != 0:
            res += l // a - 1
    
    print(res)


