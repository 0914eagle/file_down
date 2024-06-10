
def solve(num):
    num = str(num)
    n = len(num)
    if n == 1:
        return 0
    
    left = 0
    right = n - 1
    
    while left < right:
        if num[left] != num[right]:
            break
        left += 1
        right -= 1
    
    if left >= right:
        return 0
    
    left_num = int(num[left])
    right_num = int(num[right])
    
    if left_num == 9:
        left_num = 0
    else:
        left_num += 1
    
    if right_num == 9:
        right_num = 0
    else:
        right_num += 1
    
    return 1 + solve(int(num[:left] + str(left_num) + num[left+1:right] + str(right_num) + num[right+1:]))
    
num = int(input())
print(solve(num))

