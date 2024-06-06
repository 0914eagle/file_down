
#如果每一位都是X的倍数，那就不会有多余的
#例如X=6，倍数为6，12，18，24，30，36，42，48，54，60，66
#只需要不断把X扩充，不断更新就行了
import sys
import os
from io import BytesIO
input = lambda: sys.stdin.readline().rstrip('\r\n')

def main():
    X,A,B = map(int, input().split())
    string = input()

    Xstr = str(X)
    Xlen = len(Xstr)
    if Xlen == 1:
        if string.count(Xstr) == 0:
            print(0)
            return
        else:
            X = int(X)
            while X <= A:
                X += X
            ans = (B//X - A//X) + 1
            print(ans)
            return

    ans = 0
    while X <= B:
        Xs = str(X)
        ok = True
        for i in Xs:
            if i not in string:
                ok = False
                break
        if ok:
            ans += 1
        # X += 1 #这个不能这么写，因为可能会溢出
        X += X
    print(ans)

if __name__ == "__main__":
    main()
