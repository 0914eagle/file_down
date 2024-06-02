
def find_median(k, s, t):
    def get_next_char(c):
        if c == 'z':
            return 'a'
        else:
            return chr(ord(c) + 1)
    
    median = ""
    for i in range(k):
        if s[i] != t[i]:
            median += get_next_char(s[i])
            break
        else:
            median += s[i]
    
    return median

# Read input
k = int(input())
s = input()
t = input()

# Find and print the median
print(find_median(k, s, t))
