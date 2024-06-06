
import re
line=input()
words=re.split(r'[ ,.!?]+',line)
syllables=[0]*len(words)
for i in range(len(words)):
    word=words[i]
    for j in range(len(word)):
        if word[j] in ['a','e','i','o','u','y']:
            syllables[i]+=1
            if word[j] in ['e']:
                if j+1<len(word) and word[j+1]=='l':
                    if j+2<len(word) and word[j+2] in ['a','e','i','o','u','y']:
                        syllables[i]-=1
                    else:
                        syllables[i]-=2
                else:
                    syllables[i]-=1
        else:
            if j>1 and word[j-1:j+1]=='qu':
                syllables[i]+=1
v=0
for i in range(len(syllables)):
    v+=syllables[i]
if v==17:
    for i in range(len(syllables)):
        if syllables[i]==1:
            syllables[i]=0
        else:
            syllables[i]=1
    v=0
    for i in range(len(syllables)):
        v+=syllables[i]
    if v==17:
        print(line)
        exit()
    for i in range(len(syllables)):
        if syllables[i]==1:
            syllables[i]=0
        else:
            syllables[i]=1
    v=0
    for i in range(len(syllables)):
        v+=syllables[i]
    if v==17:
        print(line)
        exit()
if v!=17:
    print(line)
    exit()
cnt=0
for i in range(len(syllables)):
    if syllables[i]==0:
        if cnt==5:
            print(line)
            exit()
    else:
        cnt+=1
print(line)
