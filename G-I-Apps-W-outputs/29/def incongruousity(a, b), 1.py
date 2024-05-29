
def incongruousity(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    return count

def find_least_incongruous_alternatives(question, num_alternatives, alternatives):
    min_incongruity = float('inf')
    least_incongruous = []

    for i in range(num_alternatives):
        incongruity = 0
        for j in range(num_alternatives):
            incongruity = max(incongruity, incongruousity(alternatives[i], alternatives[j]))
        if incongruity < min_incongruity:
            min_incongruity = incongruity
            least_incongruous = [alternatives[i]]
        elif incongruity == min_incongruity:
            least_incongruous.append(alternatives[i])

    return least_incongruous

question = input().strip()
num_alternatives = int(input().strip())
alternatives = []
for _ in range(num_alternatives):
    alternatives.append(input().strip().split(', '))

for ans in find_least_incongruous_alternatives(question, num_alternatives, alternatives):
    print(", ".join(ans))
```
