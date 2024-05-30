
def round_abbrev(n):
    return "ABC" + str(n).rjust(3, '0')

n = int(input())
print(round_abbrev(n))

