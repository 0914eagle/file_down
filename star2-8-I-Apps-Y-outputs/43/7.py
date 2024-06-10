
f, s, g, u, d = map(int, input().split())

def dfs(pos, cnt):
    if pos == g:
        return cnt
    
    if pos + u <= f:
        ret = dfs(pos + u, cnt + 1)
        if ret is not None:
            return ret
    
    if pos - d >= 1:
        ret = dfs(pos - d, cnt + 1)
        if ret is not None:
            return ret
    
    return None

result = dfs(s, 0)
if result is None:
    print("use the stairs")
else:
    print(result)

