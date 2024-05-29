
def person_info(func):
    def sort_by_age(people):
        return sorted(people, key=lambda x: (int(x[2]), people.index(x)))

    @person_info
    def print_names(n, people):
        for person in people:
            if person[3] == 'M':
                print(f"Mr. {person[0]} {person[1]}")
            else:
                print(f"Ms. {person[0]} {person[1]}")

    n = int(input())
    people = []
    for _ in range(n):
        person = input().split()
        people.append(person)

    print_names(n, people)

