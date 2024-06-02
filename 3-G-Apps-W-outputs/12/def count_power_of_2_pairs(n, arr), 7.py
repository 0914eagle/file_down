
def count_power_of_2_pairs(n, arr):
    count = 0
    power_of_2 = set()
    
    for i in range(31):  # 2^31 is the largest power of 2 within the given constraints
        power_of_2.add(1 << i)
    
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    for i in range(n):
        for j in range(i+1, n):
            if (arr[i] + arr[j]) in power_of_2:
                count += 1
    
    for num in freq:
        if freq[num] > 1 and (num * 2) in power_of_2:
            count += (freq[num] * (freq[num] - 1)) // 2
    
    return count

# Input reading and function call
n = int(input())
arr = list(map(int, input().split()))

result = count_power_of_2_pairs(n, arr)
print(result)
