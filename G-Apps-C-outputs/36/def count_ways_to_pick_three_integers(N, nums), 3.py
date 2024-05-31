
def count_ways_to_pick_three_integers(N, nums):
    count = 0
    sum_dict = {}

    for i in range(N):
        for j in range(i+1, N):
            target_sum = nums[i] + nums[j]
            if target_sum in sum_dict:
                count += sum_dict[target_sum]
            if target_sum not in sum_dict:
                sum_dict[target_sum] = 1
            else:
                sum_dict[target_sum] += 1
    
    return count

# Input parsing
N = int(input())
nums = list(map(int, input().split()))

# Call the function with the input values
result = count_ways_to_pick_three_integers(N, nums)
print(result)
