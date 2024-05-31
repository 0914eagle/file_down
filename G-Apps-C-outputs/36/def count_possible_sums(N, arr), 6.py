
def count_possible_sums(N, arr):
    count = 0
    sum_dict = {}

    for i in range(N):
        for j in range(i+1, N):
            curr_sum = arr[i] + arr[j]
            if curr_sum in sum_dict:
                sum_dict[curr_sum] += 1
            else:
                sum_dict[curr_sum] = 1

    for k in range(N):
        if arr[k] in sum_dict:
            count += sum_dict[arr[k]]
    
    return count

# Read input
N = int(input())
arr = list(map(int, input().split()))

# Call the function and print the output
result = count_possible_sums(N, arr)
print(result)
