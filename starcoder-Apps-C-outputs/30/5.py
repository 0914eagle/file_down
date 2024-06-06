
from collections import defaultdict

def isPossible(dic,s,string):
    if len(s) == 0 and len(string) == 0:
        return True

    if len(s) == 0:
        return False

    for i in range(len(s)+1):
        if s[0:i] in dic:
            if isPossible(dic,s[i:],string):
                return True
    return False

def backtrack(dic,s,string,res):
    if len(s) == 0 and len(string) == 0:
        return True

    if len(s) == 0:
        return False

    for i in range(len(s)+1):
        if s[0:i] in dic:
            res.append(s[0:i])
            if backtrack(dic,s[i:],string,res):
                return True
            res.pop()
    return False

if __name__ == "__main__":
    s = input()
    n = int(input())
    dic = defaultdict(int)
    for i in range(n):
        dic[input()] = 1

    if isPossible(dic,s,s):
        res = []
        backtrack(dic,s,s,res)
        print(' '.join(res))
    else:
        print("impossible")
