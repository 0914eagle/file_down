
def abbreviate_contest_name(s):
    words = s.split()
    contest_name = words[1]
    abbreviation = f"{contest_name[0]}C"
    print(abbreviation)

# Sample Input
contest_name = "AtCoder Beginner Contest"
abbreviate_contest_name(contest_name)
```
