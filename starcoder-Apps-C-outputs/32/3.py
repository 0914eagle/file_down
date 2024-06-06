
s = input()

# case 1
if s.count('a') == s.count('c') or s.count('a') == s.count('b') or s.count('c') == s.count('b'):
    print("YES")
# case 2
elif s.count('a') > 0 and s.count('b') > 0 and s.count('c') > 0:
    if 'a' in s and 'b' in s and 'c' in s:
        print("YES")
    else:
        print("NO")
else:
    print("NO")

