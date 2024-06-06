
def solve(s):
    dict1 = {"be":1,"our":1,"rum":1,"will":1,"dead":1,"hook":1,"ship":1,"blood":1,"sable":1,"avenge":1,"parrot":1,"captain":1}
    s = s.replace(' ', '')
    n = len(s)
    for i in range(n):
        for j in range(n):
            if s[j]>s[i]:
                s[j],s[i] = s[i],s[j]
    # print(s)
    # s = list(s)
    # print(s)
    for i in range(n):
        for j in range(n):
            if s[j]>s[i]:
                s[j],s[i] = s[i],s[j]
    for i in range(n):
        if s[i] in dict1:
            dict1[s[i]] -= 1
            if dict1[s[i]] == -1:
                return "Impossible"
    print(s)
s = "ex eoii jpxbmx cvz uxju sjzzcn jzz"
s = s.split(' ')
s = [i.split('') for i in s]
s = solve(s)
print(s)
