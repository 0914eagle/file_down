
n=int(input())
s=input()
i=0
cnt=0
while i<n:
    if s[i]=='P':
        j=i+1
        while j<n:
            if s[j]=='*':
                cnt+=j-i
                s=s[0:i]+s[i:j].replace('*','')+s[j:]
                break
            j+=1
        i=j
    else:
        i+=1
print(cnt)
