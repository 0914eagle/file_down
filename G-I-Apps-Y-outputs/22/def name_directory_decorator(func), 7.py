
def name_directory_decorator(func):
    def sort_names_by_age(people):
        sorted_people = sorted(people, key=lambda x: x[2])
        for person in sorted_people:
            title = "Mr." if person[3] == 'M' else "Ms."
            full_name = f"{title} {person[0]} {person[1]}"
            print(full_name)
    return sort_names_by_age

@name_directory_decorator
def print_names(people):
    for person in people:
        yield person

# Input
N = int(input())
people = []
for _ in range(N):
    first_name, last_name, age, sex = input().split()
    people.append((first_name, last_name, int(age), sex))

# Output
print_names(people)
```
