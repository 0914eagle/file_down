
# https://codeforces.com/contest/1182/problem/B

# Wrong Answer 
n, l, r = map(int, input().split())
if n==0:
  print(0)
else:
  bin_n = bin(n)[2:][::-1]
  sum = 0
  for i in range(l-1, r):
    if bin_n[i]=='1':
      sum += 1
  print(sum)

