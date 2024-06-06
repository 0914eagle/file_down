
n=int(input())
s=input()
m=s.count('M')
c=s.count('C')
y=s.count('Y')
if (m>=2 and c>=1 and y>=1) or (m>=1 and c>=2 and y>=1) or (m>=1 and c>=1 and y>=2):
  print('Yes')
else:
  print('No')
