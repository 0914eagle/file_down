
# 100%

def main():
    s = input()
    n = int(input())
    words = [input() for _ in range(n)]

    def dfs(i, j, path):
        if i == len(s) and j == len(words):
            return path
        if i == len(s) or j == len(words):
            return None
        for k in range(j, len(words)):
            if s[i:i+len(words[k])] == words[k]:
                res = dfs(i+len(words[k]), k+1, path+[words[k]])
                if res:
                    return res
        return None

    res = dfs(0, 0, [])
    if res:
        print(' '.join(res))
    else:
        print('impossible')

main()
