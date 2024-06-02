
def check_partition_possible(n, arr):
    even_nums = []
    odd_nums = []
    
    for num in arr:
        if num % 2 == 0:
            even_nums.append(num)
        else:
            odd_nums.append(num)
    
    if len(even_nums) % 2 == 0 and len(odd_nums) % 2 == 0:
        return "YES"
    
    even_nums.sort()
    odd_nums.sort()
    
    for i in range(len(even_nums) - 1):
        if even_nums[i+1] - even_nums[i] == 1:
            return "YES"
    
    for i in range(len(odd_nums) - 1):
        if odd_nums[i+1] - odd_nums[i] == 1:
            return "YES"
    
    return "NO"

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result = check_partition_possible(n, arr)
    print(result)
