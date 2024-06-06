
s = input()
n = len(s)
for i in range(1,n):
    for j in range(i+1,n):
        if int(s[:i])+int(s[i:j])==int(s[j:]):
            print(s[:i]+'+'+s[i:j]+'='+s[j:])
            break
