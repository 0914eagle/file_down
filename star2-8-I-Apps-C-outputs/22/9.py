
a, b = map(int, input().split())
l = int(input())

insecure = 2 * (l - 1) - 2
secure = 2 * (a + 1 + b) - 4
super_secure = 2 * (a + 1 + b) - 2

print(insecure)
print(secure)
print(super_secure)

