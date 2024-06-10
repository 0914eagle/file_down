
def gcd(l):
  if len(l) == 1:
    return l[0]
  else:
    return gcd([l[1], l[0] % l[1]])
    
n = int(input())
s = [int(i) for i in input().split()]

counter = 0
for i in range(n):
  if gcd(s[i:]) == 1:
    counter += 1
  else:
    break
    
print(counter)

