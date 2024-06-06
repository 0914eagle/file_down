
# 1. 先找出所有符合条件的数
# 2. 再从中找出最大的数
# 3. 若无符合条件的数，则返回 -1

def find_max_num(l, r):
    # 找出所有符合条件的数
    nums = []
    for i in range(l, r+1):
        if is_valid(i):
            nums.append(i)
    # 若无符合条件的数，则返回 -1
    if not nums:
        return -1
    # 从中找出最大的数
    return max(nums)

def is_valid(num):
    # 若有重复的数字，则返回 False
    if len(set(str(num))) < len(str(num)):
        return False
    return True

if __name__ == '__main__':
    l, r = map(int, input().split())
    print(find_max_num(l, r))
