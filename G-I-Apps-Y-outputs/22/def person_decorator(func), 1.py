
def person_decorator(func):
    def inner(person):
        title = 'Mr.' if person[3] == 'M' else 'Ms.'
        return func(title, person)
    return inner

@person_decorator
def print_person(title, person):
    print(title, person[0], person[1])

def name_directory(people):
    sorted_people = sorted(people, key=lambda x: (int(x[2]), people.index(x)))
    for person in sorted_people:
        print_person(person)

# Input
N = int(input())
people = []
for _ in range(N):
    person = input().split()
    people.append(person)

# Output
name_directory(people)
```
