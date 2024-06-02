
n = int(input())
s = input()

# count the number of each color
r = s.count('R')
g = s.count('G')
b = s.count('B')

# find the most frequent color
max_color = max(r, g, b)

# find the number of colors that are not the most frequent color
num_colors = 0
if r != max_color:
    num_colors += 1
if g != max_color:
    num_colors += 1
if b != max_color:
    num_colors += 1

# if there are only two colors, the number of recolors is the difference
# between the number of lamps and the number of colors
if num_colors == 2:
    print(n - num_colors)
# otherwise, the number of recolors is the difference between the number
# of lamps and the most frequent color
else:
    print(n - max_color)

# create the diverse garland
t = ''
for i in range(n):
    if s[i] != 'R':
        t += 'R'
    elif s[i] != 'G':
        t += 'G'
    else:
        t += 'B'

print(t)


a, b = map(int, input().split())
print(a + b)
# 
