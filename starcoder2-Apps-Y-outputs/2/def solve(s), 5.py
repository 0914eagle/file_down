
def solve(s):
    ans = ""
    for c in s:
        if c == "B":
            ans = ans[:-1]
        else:
            ans += c
    return ans

s = input()
print(solve(s))

