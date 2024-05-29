
def abbreviate_contest_name(name):
    words = name.split()
    first_char = words[0][0]
    abbreviation = first_char + 'x' + 'C'
    print(abbreviation)

contest_name = input()
abbreviate_contest_name(contest_name)
```
