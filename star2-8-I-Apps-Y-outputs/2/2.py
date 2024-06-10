
N = int(input())
a = list(map(int, input().split()))

a = sorted(a)

left = 0
right = N-1

res = 0

while left < right:
    res += a[right] - a[left]
    left += 1
    right -= 1
    
print(res)

