
def count_ways_to_pick_three_integers(N, arr):
    count = 0
    sum_count = {}
    
    for i in range(N):
        for j in range(i+1, N):
            sum_val = arr[i] + arr[j]
            if sum_val in sum_count:
                count += sum_count[sum_val]
                
            if sum_val not in sum_count:
                sum_count[sum_val] = 1
            else:
                sum_count[sum_val] += 1
    
    return count

# Read input
N = int(input())
arr = list(map(int, input().split()))

# Call the function and output the result
print(count_ways_to_pick_three_integers(N, arr))
