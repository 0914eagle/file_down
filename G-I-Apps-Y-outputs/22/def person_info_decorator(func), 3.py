
def person_info_decorator(func):
    def wrapper(person):
        title = 'Mr.' if person[3] == 'M' else 'Ms.'
        return func(f"{title} {person[0]} {person[1]}")
    return wrapper

@person_info_decorator
def print_person_name(name):
    print(name)

n = int(input())
people = []
for _ in range(n):
    person = input().split()
    person[2] = int(person[2])  # convert age to integer
    people.append(person)

sorted_people = sorted(people, key=lambda x: (x[2], people.index(x)))
for person in sorted_people:
    print_person_name(person)

```
