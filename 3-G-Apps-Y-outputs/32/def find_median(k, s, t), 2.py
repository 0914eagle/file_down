
def find_median(k, s, t):
    def next_char(c):
        return chr(ord(c) + 1) if c != 'z' else 'a'
    
    median = ""
    for i in range(k):
        if s[i] == t[i]:
            median += s[i]
        else:
            median += next_char(s[i])
            break
    
    return median

# Read input
k = int(input())
s = input()
t = input()

# Find and print the median
print(find_median(k, s, t))
