
def name_directory_decorator(func):
    def wrapper(people):
        sorted_people = sorted(people, key=lambda x: (x[2], people.index(x)))
        return func(sorted_people)
    return wrapper

@name_directory_decorator
def print_names(people):
    for person in people:
        title = "Mr." if person[3] == 'M' else "Ms."
        print(f"{title} {person[0]} {person[1]}")

# Input
N = int(input())
people = []
for _ in range(N):
    person_info = input().split()
    people.append((person_info[0], person_info[1], int(person_info[2]), person_info[3]))

print_names(people)
```
