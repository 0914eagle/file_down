
def solve(s):
    ans = []
    for i in s:
        if i == 'B':
            if ans:
                ans.pop()
        else:
            ans.append(i)
    return ''.join(ans)

s = input()
print(solve(s))

