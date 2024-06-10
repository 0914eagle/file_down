
n = int(input())
a = list(map(int, input().split()))
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)
lcm = 1
for x in a:
    lcm = (lcm * x) // gcd(lcm, x)
if lcm == 1:
    print(-1)
else:
    print(sum(map(lambda x: (lcm - 1) % x, a)))

