
from collections import defaultdict

def book_circle(boys, girls):
    book_to_students = defaultdict(set)
    for boy in boys:
        for book in boys[boy]:
            book_to_students[book].add(boy)
    for girl in girls:
        for book in girls[girl]:
            book_to_students[book].add(girl)
    book_to_students = {book: students for book, students in book_to_students.items() if len(students) > 1}
    book_to_students = {book: students for book, students in book_to_students.items() if len(students) == len(set(students))}
    presentation_count = 0
    while book_to_students:
        book, students = book_to_students.popitem()
        presentation_count += 1
        for book, students_read in book_to_students.copy().items():
            if students.issubset(students_read):
                del book_to_students[book]

    return presentation_count

