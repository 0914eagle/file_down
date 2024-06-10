
from itertools import groupby
def factor(s):
groups = groupby(s)
factors = []
for k, g in groups:
factors.append((k, len(list(g))))
return factors
def factorize(s):
if len(s) == 1:
return s
factors = factor(s)
min_factor = factors[0]
for f in factors:
if f[1] < min_factor[1]:
min_factor = f
factor_str = min_factor[0] * min_factor[1]
factor_str = '(' + factor_str + ')'
factor_str += str(len(s) // len(factor_str))
return factor_str
def factorize_rec(s):
if len(s) == 1:
return s
factors = factor(s)
min_factor = factors[0]
for f in factors:
if f[1] < min_factor[1]:
min_factor = f
factor_str = min_factor[0] * min_factor[1]
factor_str = '(' + factor_str + ')'
factor_str += str(len(s) // len(factor_str))
return factorize_rec(factor_str)
def main():
s = input()
print(len(factorize_rec(s)))
if __name__ == '__main__':
main()

