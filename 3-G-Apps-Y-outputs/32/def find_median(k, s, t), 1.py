
def find_median(k, s, t):
    def get_next_char(char):
        if char == 'z':
            return 'a'
        else:
            return chr(ord(char) + 1)
    
    median = ""
    for i in range(k):
        if s[i] != t[i]:
            median += get_next_char(s[i])
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
