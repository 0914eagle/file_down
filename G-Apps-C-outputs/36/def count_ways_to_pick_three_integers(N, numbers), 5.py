
def count_ways_to_pick_three_integers(N, numbers):
    count = 0
    sums = set()
    
    for i in range(N):
        for j in range(i+1, N):
            if numbers[i] + numbers[j] in sums:
                count += 1
            else:
                sums.add(numbers[i] + numbers[j])
    
    return count

# Input processing
N = int(input())
numbers = list(map(int, input().split()))

# Call the function and print the result
result = count_ways_to_pick_three_integers(N, numbers)
print(result)
