
n = int(input())

hirings = [0] * (n+1)
firings = [0] * (n+1)

for i in range(n):
    f, h = map(int, input().split())
    firings[i+1] = f
    hirings[i+1] = h

def is_possible(k):
    used = [0] * (k+1)
    curr = 0
    for i in range(1, n+1):
        curr += hirings[i]
        curr -= firings[i]
        
        for j in range(curr, 0, -1):
            if used[j] == 0:
                used[j] = 1
                break
        
    return curr == 0

left, right = 1, n
while left <= right:
    mid = (left + right) // 2
    
    if is_possible(mid):
        right = mid - 1
    else:
        left = mid + 1

print(left)

used = [0] * (left+1)
curr = 0
for i in range(1, n+1):
    curr += hirings[i]
    curr -= firings[i]
    
    for j in range(curr, 0, -1):
        if used[j] == 0:
            used[j] = 1
            print(j, end=' ')
            break

