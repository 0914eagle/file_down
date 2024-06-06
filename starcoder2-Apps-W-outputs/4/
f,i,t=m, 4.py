
f,i,t=map(int,input().split())
a=[input() for _ in range(f)]
print(sum(a.count('Y')>=t for a in zip(*a)))
