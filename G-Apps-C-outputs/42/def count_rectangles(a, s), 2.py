
def count_rectangles(a, s):
    count = 0
    n = len(s)
    
    prefix_sum = [0]
    for i in range(n):
        prefix_sum.append(prefix_sum[-1] + int(s[i]))
    
    b = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(i, n):
            b[i][j] = int(s[i]) * int(s[j])
    
    for i in range(n):
        for j in range(i, n):
            curr_sum = prefix_sum[j+1] - prefix_sum[i]
            if b[i][j] == a and curr_sum % a == 0:
                count += 1
    
    return count

# Input
a = int(input())
s = input().strip()

# Call the function
result = count_rectangles(a, s)
print(result)
