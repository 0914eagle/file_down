
def abbreviate_contest_name(s):
    first_char = s[0]
    return first_char + 'x' + 'C'


contest_name = input().split()
result = abbreviate_contest_name(contest_name[1])
print(result)
```
