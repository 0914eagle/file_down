
s=input()
vowel="aeiou"
s1="YES"
for i in range(len(s)):
    if s[i] in vowel:
        if s[i+1] not in vowel:
            s1="NO"
            break
    elif s[i]!="n":
        if s[i+1] in vowel:
            s1="NO"
            break
    if s[i]=="n":
        if s[i+1] in vowel:
            s1="NO"
            break
print(s1)
