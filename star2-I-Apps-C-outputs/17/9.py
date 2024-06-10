
def solve(s):
    n = len(s)
    if n == 1:
        return 0
    if n == 2:
        if s[0] == s[1]:
            return 0
        else:
            return 1
    left = 0
    right = n - 1
    while left < right and s[left] == s[right]:
        left += 1
        right -= 1
    if left >= right:
        return 0
    else:
        return 1 + min(solve(s[left+1:right+1]), solve(s[left:right]))

s = input()
print(solve(s))

