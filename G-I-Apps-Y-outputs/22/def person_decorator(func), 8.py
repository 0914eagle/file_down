
def person_decorator(func):
    def wrapper(person):
        title = "Mr." if person[-1] == 'M' else "Ms."
        return title + " " + func(person)
    return wrapper

@person_decorator
def format_name(person):
    return " ".join(person[:-1])

def build_name_directory(people):
    sorted_people = sorted(people, key=lambda x: int(x[2]))
    for person in sorted_people:
        print(format_name(person))

# Sample input
N = 3
people = [
    ["Henry", "Davids", "30", "M"],
    ["Mary", "George", "25", "F"],
    ["John", "Smith", "25", "M"]
]

build_name_directory(people)
```
