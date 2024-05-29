
def person_format(func):
    def sort_by_age(people):
        sorted_people = sorted(people, key=lambda x: x[2])
        for person in sorted_people:
            if person[3] == 'M':
                print("Mr. {} {}".format(person[0], person[1]))
            else:
                print("Ms. {} {}".format(person[0], person[1]))
    return sort_by_age

@person_format
def format_names(people):
    pass

# Input
N = int(input())
people = []
for _ in range(N):
    first_name, last_name, age, sex = input().split()
    age = int(age)
    people.append((first_name, last_name, age, sex))

# Output
format_names(people)
```
