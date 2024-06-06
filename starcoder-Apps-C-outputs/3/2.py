
def main():
    n = int(input())
    nums = list(map(int, input().split()))
    ans = []
    for i in range(n):
        if nums[i] > nums[i - 1]:
            ans.append([i, i - 1])
            nums[i] -= nums[i - 1]
            nums[i - 1] = 0
    for i in range(n):
        if nums[i] < 0:
            ans.append([i, i + 1])
            nums[i + 1] += nums[i]
            nums[i] = 0
    print(len(ans))
    for x, y in ans:
        print(x + 1, y + 1)


if __name__ == '__main__':
    main()
