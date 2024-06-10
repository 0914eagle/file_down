
def usaico(n, s):
    return max(s.count("01"), s.count("10"))

n = int(input())
s = input()
print(usaico(n, s))

