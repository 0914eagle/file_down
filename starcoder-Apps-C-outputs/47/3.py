
n,k=map(int,input().split())
if n==k:
    print(''.join([chr(ord('a')+i) for i in range(n)]))
else:
    s=list(map(chr,range(97,97+k)))
    s=s+s
    print(''.join(s[:n]))
