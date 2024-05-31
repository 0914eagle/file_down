
def count_permutations(n, know_matrix):
    ans = [0] * (1 << (n - 1))
    
    for i in range(1, 1 << n):
        bin_str = bin(i)[2:].zfill(n)
        count = 0
        
        for j in range(n):
            if bin_str[j] == '1':
                for k in range(j + 1, n):
                    if bin_str[k] == '1' and know_matrix[j][k] == '0':
                        count += 1
        
        ans[count] += 1
    
    return ans

# Read input
n = int(input())
know_matrix = [input() for _ in range(n)]

# Calculate and print the output
output = count_permutations(n, know_matrix)
print(*output)
