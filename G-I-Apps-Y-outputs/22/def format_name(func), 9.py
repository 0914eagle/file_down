
# Custom decorator to format the name based on sex
def format_name(func):
    def wrapper(person):
        if person['sex'] == 'M':
            title = 'Mr.'
        else:
            title = 'Ms.'
        return title + ' ' + func(person)
    return wrapper

# Function to extract names in the required format and sort by age
@format_name
def get_formatted_name(person):
    return person['first_name'] + ' ' + person['last_name']

if __name__ == '__main__':
    n = int(input())
    people = []
    for _ in range(n):
        first_name, last_name, age, sex = input().split()
        person = {'first_name': first_name, 'last_name': last_name, 'age': int(age), 'sex': sex}
        people.append(person)

    sorted_people = sorted(people, key=lambda x: (x['age']))

    for person in sorted_people:
        print(get_formatted_name(person))
