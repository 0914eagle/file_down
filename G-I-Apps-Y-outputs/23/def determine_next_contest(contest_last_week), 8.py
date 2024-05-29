
def determine_next_contest(contest_last_week):
    if contest_last_week == "ABC":
        return "ARC"
    elif contest_last_week == "ARC":
        return "ABC"

# Input last week's contest type
contest_last_week = input().strip()

# Determine and print this week's contest type
print(determine_next_contest(contest_last_week))
```
