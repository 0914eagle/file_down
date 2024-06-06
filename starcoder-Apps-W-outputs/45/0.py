
#encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

s_1 = sys.stdin.readline().strip()
s_2 = sys.stdin.readline().strip()

total = 1
for i in range(len(s_1)):
    if s_2[i] == '+':
        total += 1
    elif s_2[i] == '-':
        total -= 1

if total == 0:
    print 1.0
else:
    print 0.0
