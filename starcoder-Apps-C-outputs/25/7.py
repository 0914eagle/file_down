
# 代码
import sys
from copy import deepcopy

def fun():
    nr,nc,n,m = map(int,input().split())
    _info = sys.stdin.readlines()
    info = []
    for _i in _info:
        if _i != '\n':
            info.append(list(map(int, _i.strip().split(' '))))

    # (x1,y1),(x2,y2)
    del_info = []
    for i in range(n):
        del_info.append(info[i])
    del_info.sort(key = lambda x:x[0])
    del_info.sort(key = lambda x:x[1])
    del_info = del_info[::-1]

    keep_info = []
    for i in range(m,n+m):
        keep_info.append(info[i])
    keep_info.sort(key = lambda x:x[0])
    keep_info.sort(key = lambda x:x[1])
    keep_info = keep_info[::-1]

    #print(del_info,keep_info)

    total = nr * nc
    res = total
    while del_info:
        del_info = del_info[::-1]
        del_x1,del_y1 = del_info[-1]
        for i in range(len(keep_info)):
            x1,y1 = keep_info[i]
            if x1 <= del_x1 and y1 <= del_y1:
                if i == len(keep_info) - 1:
                    keep_info.pop()
                else:
                    keep_info = keep_info[:i]+keep_info[i+1:]
                break
        else:
            x2 = del_x1 + 15
            y2 = del_y1 + 9
            res = min(res,x2*y2)
            del_info.pop()
    return res

while True:
    try:
        print(fun())
    except:
        break
