
def person_info_decorator(func):
    def wrapper(person):
        title = 'Mr.' if person[3] == 'M' else 'Ms.'
        return func(f"{title} {person[0]} {person[1]}")
    return wrapper

@person_info_decorator
def print_person_name(person):
    print(person)

if __name__ == "__main__":
    num_people = int(input())
    people = []
    for _ in range(num_people):
        first_name, last_name, age, sex = input().split()
        people.append((first_name, last_name, int(age), sex))
    
    sorted_people = sorted(people, key=lambda x: (x[2], people.index(x)))
    for person in sorted_people:
        print_person_name(person)
```
