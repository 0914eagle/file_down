
def can_be_printed(s, t):
    if len(t) < len(s):
        return "NO"
    
    s_index = 0
    t_index = 0
    while s_index < len(s) and t_index < len(t):
        if s[s_index] == t[t_index]:
            s_index += 1
        t_index += 1
    
    if s_index == len(s):
        return "YES"
    else:
        return "NO"

# Read input
n = int(input())
for _ in range(n):
    s = input().strip()
    t = input().strip()
    result = can_be_printed(s, t)
    print(result)
