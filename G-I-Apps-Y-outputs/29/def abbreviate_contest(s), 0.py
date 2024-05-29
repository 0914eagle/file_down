
def abbreviate_contest(s):
    x = s.split()[0][0]
    return f"A{x}C"

contest_name = input()
print(abbreviate_contest(contest_name))
```
