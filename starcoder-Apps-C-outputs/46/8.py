
n = int(input())
x = bin(n)[2:]
x = x[::-1]
# print(x)
print(x.count('1'))
