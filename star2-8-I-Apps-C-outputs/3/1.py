
n = int(input())
l = list(map(int,input().split()))
max_sum = l[0]
min_sum = l[-1]
max_index = 0
min_index = n-1
max_damage = 0
for i in range(n):
  max_sum += l[i]
  min_sum += l[n-i-1]
  if max_sum < l[i+1]:
    max_damage += (l[i+1] - max_sum)
    max_index = i+1
  if min_sum < l[n-i-2]:
    max_damage += (l[n-i-2] - min_sum)
    min_index = n-i-2
print(max_damage,max_index)

