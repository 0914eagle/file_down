
def abbreviate_contest_name(name):
    words = name.split()
    first_char = words[0][0]
    abbreviation = f'{first_char}C'
    print(abbreviation)

contest_name = "AtCoder Beginner Contest"
abbreviate_contest_name(contest_name)
```
