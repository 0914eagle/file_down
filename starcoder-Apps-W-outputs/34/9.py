
# your code goes here
n = int(input())
s1 = ""
s2 = ""
for i in range(n):
    x, y = input().split()
    if y == '0':
        s1 += 'move {} {}\n'.format(x, len(s2) + len(s1) + 1)
    else:
        s2 += 'move {} {}\n'.format(x, len(s2) + 1)
print(len(s1) + len(s2) - 1)
print(s2 + s1, end = '')
