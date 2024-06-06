
import sys
import math

n,g = list(map(int,input().split()))
list_one = []
list_two = []
for _ in range(n):
    a,b = map(int,input().split())
    list_one.append(a)
    list_two.append(b)
for i in range(n):
    list_one[i] = list_one[i] * list_two[i]
list_three = []
for i in range(len(list_two)):
    list_three.append([list_one[i],list_two[i]])
list_three.sort(reverse = True)
for i in range(len(list_three)):
    list_three[i][0] = list_three[i][0] // list_three[i][1]
i = 0
price = 0
while(i<n):
    if list_three[i][1] <= g:
        price += list_three[i][0]
        g -= list_three[i][1]
    else:
        price += g*list_three[i][0]
        break
    i += 1
print(price)
