
import sys
from collections import defaultdict

def get_num_of_open_brackets(s):
    ans = 0
    for ch in s:
        ans += 1 if ch == '(' else -1
    return ans

# check if concatenation is a valid bracket sequence
def is_valid(a, b):
    return get_num_of_open_brackets(a) + get_num_of_open_brackets(b) >= 0

n = int(sys.stdin.readline())
# use two default dictionaries to store the number of occurences of 
# non-negative and negative prefixes of each bracket sequence
pre_a, pre_b = defaultdict(int), defaultdict(int)
for i in range(n):
    s = sys.stdin.readline().rstrip()
    num_of_open_brackets = get_num_of_open_brackets(s)
    pre_a[num_of_open_brackets] += 1
for i in range(n):
    s = sys.stdin.readline().rstrip()
    num_of_open_brackets = get_num_of_open_brackets(s)
    pre_b[-num_of_open_brackets] += 1

# number of pairs that satisfy the conditions
ans = 0
for i in pre_a:
    if i in pre_b:
        ans += pre_a[i] * pre_b[i]
for i in pre_b:
    if -i in pre_a:
        ans += pre_a[-i] * pre_b[i]

print(ans)
