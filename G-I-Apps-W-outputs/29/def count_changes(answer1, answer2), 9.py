
def count_changes(answer1, answer2):
    changes = 0
    parts1 = answer1.split(", ")
    parts2 = answer2.split(", ")
    
    for i in range(len(parts1)):
        if parts1[i] != parts2[i]:
            changes += 1
    
    return changes

def min_incongruous_alternative(question, n, answers):
    incongruousity = {answer: 0 for answer in answers}

    for i in range(n):
        for j in range(i+1, n):
            changes = count_changes(answers[i], answers[j])
            incongruousity[answers[i]] = max(incongruousity[answers[i]], changes)
            incongruousity[answers[j]] = max(incongruousity[answers[j]], changes)

    min_max_changes = min(incongruousity.values())

    result = [answer for answer, changes in incongruousity.items() if changes == min_max_changes]
    return result

# Input
question = "The flag of the empire Angola?"
n = 4
answers = [
    "Green stripe, black stripe, yellow",
    "Red stripe, black stripe, yellow",
    "Red stripe, black stripe, white",
    "Red stripe, green stripe, yellow"
]

# Output
output = min_incongruous_alternative(question, n, answers)
for answer in output:
    print(answer)
```

