
def abbreviate_contest_name(s):
    if s[0].isupper():
        return s[0] + 'C'
    return ""

contest_name = "AtCoder Beginner Contest"
print(abbreviate_contest_name(contest_name))
