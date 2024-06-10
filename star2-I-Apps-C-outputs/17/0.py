
def solve(num):
    num = str(num)
    n = len(num)
    if n == 1:
        return 0
    
    left = num[:n//2]
    right = num[n//2:]
    
    if left == right:
        return 0
    
    left = list(left)
    right = list(right)
    
    for i in range(len(left)):
        if left[i] != right[i]:
            break
    
    steps = 0
    
    if left[i] < right[i]:
        steps += ord(right[i]) - ord(left[i])
        left[i] = right[i]
    else:
        steps += ord(left[i]) - ord(right[i])
        right[i] = left[i]
    
    for j in range(i+1, len(left)):
        if left[j] != '0':
            steps += ord('9') - ord(left[j]) + 1
            left[j] = '0'
    
    for j in range(i+1, len(right)):
        if right[j] != '0':
            steps += ord('9') - ord(right[j]) + 1
            right[j] = '0'
    
    return steps

num = int(input())
print(solve(num))

