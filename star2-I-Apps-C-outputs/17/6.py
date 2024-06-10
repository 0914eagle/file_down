
def solve(s):
    n = len(s)
    left = 0
    right = n-1
    count = 0
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            if s[left] < s[right]:
                s = str(int(s) + 10**(n-left-1))
                count += 1
            else:
                s = str(int(s) - 10**(n-right-1))
                count += 1
            left = 0
            right = n-1
    return count

s = input()
print(solve(s))

