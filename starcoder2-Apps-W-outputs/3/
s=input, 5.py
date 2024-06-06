
s=input()
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if int(s[:i])+int(s[i:j])==int(s[j:]):
            print(s[:i]+'+'+s[i:j]+'='+s[j:])
