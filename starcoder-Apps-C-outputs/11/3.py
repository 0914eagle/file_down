
#!/usr/bin/env python
# coding=utf-8
h,m,s,t1,t2 = map(int, raw_input().split())
if t1 > t2:
	t2 += 12
if t1==12 and t2 ==1:
	print "NO"
elif t1==1 and t2 ==12:
	print "YES"
elif t1==12 and t2!=1:
	print "YES"
elif t1!=12 and t2==1:
	print "NO"
elif (h == t1 or h == t2) and m == 0 and s==0:
	print "NO"
elif h>t1 and h<t2:
	print "NO"
else:
	print "YES"
