
#https://www.urionlinejudge.com.br/judge/en/problems/view/1258

import sys

n = int(sys.stdin.readline())
while n > 0:
    dic = []
    input()
    dic = sys.stdin.readlines()
    dic = sorted(dic)
    dic = sorted(dic, key=lambda x: x.split()[2])
    dic = sorted(dic, key=lambda x: x.split()[1])
    dic = sorted(dic, key=lambda x: x.split()[0], reverse=True)
    for i in range(len(dic)):
        print(dic[i].strip())
    n = int(sys.stdin.readline())
    if n > 0:
        print('')

