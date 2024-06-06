


if __name__ == '__main__':
    n = int(input())
    nums = []
    example = []
    for i in range(n):
        s = input().split()
        nums.append([s[0], s[1]])
        if s[1] == '1':
            example.append([s[0], i + 1])

    nums.sort(key=lambda x: int(x[0]))  # 按文件名字典序排序
    nums.sort(key=lambda x: x[1], reverse=True)  # 按文件类型逆序排序

    # 按照要求输出
    print(len(example) + len(nums))
    for i in range(len(example)):
        print(f'move {nums[i][0]} {example[i][1]}')
    for i in range(len(nums) - 1, -1, -1):
        print(f'move {nums[i][0]} {i + 1 + len(example)}')
