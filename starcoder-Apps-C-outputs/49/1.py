

import sys

n, L, R = sys.stdin.readline().strip().split()

# n is the number that we want to find multiples of
# L and R are the lower and upper bounds of the range we are searching for multiples in

n = int(n)
L = int(L)
R = int(R)

# If n is a single digit, then the answer is simple. Just calculate the difference between L and R, and then add 1
if len(str(n)) == 1:
    ans = R - L + 1

# If n is more than a single digit, the trick here is that we want to only consider the leading digits of the
# numbers in the range L and R. The rest of the digits can be whatever they want.

# So, we first calculate the length of n and L, and then figure out how many multiples of n we have for each
# possible leading digit.
else:
    n_len = len(str(n))
    L_len = len(str(L))
    leading_digits = [int(x) for x in str(L)]
    ans = 0
    if L_len == 1:
        ans += 1
    else:
        leading_digits[L_len - 2] += 1
        for i in range(L_len - 2):
            leading_digits[i] = 0
    n_str = str(n)

    # There are two cases to consider: either n starts with a 1, or n starts with a 0. This is why there are two
    # separate loops
    while leading_digits[0] < 10:
        if n_str[0] == '0':
            if leading_digits[0] > 0:
                ans += 10**(n_len - 1)
            else:
                break
        else:
            if n_str[0] == str(leading_digits[0]):
                ans += 10**(n_len - 1)
            else:
                break
        leading_digits[0] += 1

print(ans)

