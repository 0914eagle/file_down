
s = input()
vowel = "aeiou"
ans = "YES"
for i in range(len(s)):
  if s[i] not in vowel:
    if s[i] != "n":
      if i != len(s) - 1 and s[i+1] not in vowel:
        ans = "NO"
print(ans)
