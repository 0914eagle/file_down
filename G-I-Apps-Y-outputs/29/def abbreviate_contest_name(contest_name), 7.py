
def abbreviate_contest_name(contest_name):
    words = contest_name.split()
    abbreviation = words[0][0] + 'C'
    print(abbreviation)

# Read the contest name from input
contest_name = input()

# Abbreviate the contest name
abbreviate_contest_name(contest_name)
```
