
def count_ways_to_pick_three_integers(N, arr):
    nums_map = {}
    count = 0

    for i in range(N):
        for j in range(i+1, N):
            sum_two_nums = arr[i] + arr[j]
            if sum_two_nums in nums_map:
                count += nums_map[sum_two_nums]
            nums_map.setdefault(sum_two_nums, 0)
            nums_map[sum_two_nums] += 1

    return count

# Input
N = int(input())
arr = list(map(int, input().split()))

# Output
print(count_ways_to_pick_three_integers(N, arr))
