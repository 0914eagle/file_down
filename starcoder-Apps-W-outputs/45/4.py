
p = 1
n = input().replace('?','+').count('+')
m = input().replace('?','-').count('-')
print(p/(2**n*2**m))
