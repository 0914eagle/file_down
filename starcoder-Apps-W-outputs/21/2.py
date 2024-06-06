

'''
**************************
* Author : Top20forlife   *
* Language : Python 2.7    *
***************************
'''
n,m=map(int,raw_input().split())
l=map(int,raw_input().split())
if max(l)>m:
    print 0
else:
    i=1
    for x in l:
        if x==i:
            i+=1
        elif x>i:
            i=x
        else:
            print 0
    print pow(2,n,1000000007)
