
def min_moves_to_make_equal(s, t):
    len_s = len(s)
    len_t = len(t)
    
    # Find the common prefix length
    common_prefix = 0
    while common_prefix < len_s and common_prefix < len_t and s[common_prefix] == t[common_prefix]:
        common_prefix += 1
        
    return len_s + len_t - 2 * common_prefix

# Reading input
s = input().strip()
t = input().strip()

# Calculate and output the minimum number of moves required
print(min_moves_to_make_equal(s, t))
