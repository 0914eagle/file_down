
def find_median(k, s, t):
    def next_char(c):
        return chr(ord(c) + 1) if c != 'z' else 'a'
    
    median = ""
    for i in range(k):
        if s[i] != t[i]:
            median += next_char(s[i])
            break
        else:
            median += s[i]
    
    return median

# Input
k = int(input())
s = input()
t = input()

# Output
print(find_median(k, s, t))
