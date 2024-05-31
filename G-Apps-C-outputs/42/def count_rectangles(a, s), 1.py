
def count_rectangles(a, s):
    total_rectangles = 0
    prefix_sum = [0]
    
    for i in range(len(s)):
        prefix_sum.append(prefix_sum[-1] + int(s[i]))
        
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            for k in range(j+1, len(s)):
                for l in range(k+1, len(s)):
                    rectangle_sum = prefix_sum[j+1] - prefix_sum[i] + prefix_sum[l+1] - prefix_sum[k]
                    if rectangle_sum == a:
                        total_rectangles += 1
    
    return total_rectangles

a = int(input())
s = input().strip()
result = count_rectangles(a, s)
print(result)
