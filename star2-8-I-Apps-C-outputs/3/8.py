

n=int(input())
arr=list(map(int,input().split()))
max_damage=0
damage=0
destroyed=0
for i in range(1,n-1):
if arr[i]<=arr[i-1] and arr[i]<=arr[i+1]:
damage=0
if arr[i-1]>=arr[i+1]:
damage+=arr[i-1]//arr[i]
else:
damage+=arr[i+1]//arr[i]
if damage>max_damage:
max_damage=damage
destroyed=i
print(max_damage+1,destroyed)


