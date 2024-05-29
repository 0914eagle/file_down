
def name_format_decorator(func):
    def inner(people):
        return [func(person) for person in sorted(people, key=lambda x: (x[2], people.index(x)))]
    return inner

@name_format_decorator
def format_name(person):
    title = "Mr." if person[3] == 'M' else "Ms."
    return f"{title} {person[0]} {person[1]}"

N = int(input())
people = [input().split() for _ in range(N)]

formatted_names = format_name(people)

for name in formatted_names:
    print(name)
```

