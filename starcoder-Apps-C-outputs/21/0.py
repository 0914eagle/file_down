
# 分析：由于题目限定了各元素的个数和范围，因此可以直接判断是否存在解
#       当且仅当元素个数和为偶数并且a>=b>=c>=d时存在解
#       即使存在解也可能有多种情况，可取任意一种即可
# 1. 总数为偶数
# 2. a>=b>=c>=d

n,a,b,c,d=map(int,input().split())
if n%2 or a<b or b<c or c<d:
    print('NO')
else:
    print('YES')
    res=[1]*a+[2]*b+[3]*c+[4]*d
    for i in range(len(res)-1):
        if res[i]==res[i+1]:
            res[i]-=1
    print(*res)

