
def count_rectangles(a, s):
    count = 0
    prefix_sum = [0]
    for i in range(len(s)):
        prefix_sum.append(prefix_sum[-1] + int(s[i]))

    distinct_sum = set()
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            sum_ij = prefix_sum[j+1] - prefix_sum[i]
            if sum_ij == a:
                count += 1
            elif sum_ij > a:
                break
            for k in range(i, j):
                sum_ik = prefix_sum[k+1] - prefix_sum[i]
                sum_kj = prefix_sum[j+1] - prefix_sum[k+1]
                if sum_ik + sum_kj == a:
                    if sum_ik not in distinct_sum:
                        distinct_sum.add(sum_ik)
                        count += 1
    return count

# Read input
a = int(input())
s = input().strip()

# Call the function and print the result
print(count_rectangles(a, s))
