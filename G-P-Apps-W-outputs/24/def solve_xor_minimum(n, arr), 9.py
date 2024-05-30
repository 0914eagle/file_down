
def solve_xor_minimum(n, arr):
    max_val = max(arr)
    
    # Find the position of the most significant bit in the maximum number
    msb_pos = 0
    while max_val:
        msb_pos += 1
        max_val >>= 1
    
    ans = 0
    for i in range(msb_pos-1, -1, -1):
        cur_bit = 1 << i
        new_ans = ans | cur_bit
        
        # Try setting the ith bit to 1 in all numbers and find the maximum
        new_max = max([num ^ new_ans for num in arr])
        
        if new_max < ans:
            ans = new_ans
    
    return ans

# Input reading
n = int(input())
arr = list(map(int, input().split()))

# Call the function and print the result
print(solve_xor_minimum(n, arr))
```
