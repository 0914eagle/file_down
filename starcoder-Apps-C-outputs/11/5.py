
h,m,s,t1,t2 = map(int,input().split())
print("NO" if (h*60+m)*60+s > (t1-1)*60*60 and (h*60+m)*60+s < (t2-1)*60*60 else "YES")
