
from sys import stdin

#zifra = input().split()
X,A,B = stdin.readline().split()
X = int(X)
A = int(A)
B = int(B)

digits = list(input())
#print(digits)

mnozici = []

for i in range(A, B+1):
    if i % X == 0:
        mnozici.append(i)

#print(mnozici)

count = 0
for i in mnozici:
    for digit in str(i):
        if digit not in digits:
            break
    else:
        count += 1

print(count)
