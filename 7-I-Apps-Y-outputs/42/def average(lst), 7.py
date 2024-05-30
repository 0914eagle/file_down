
from collections import namedtuple

def average(lst):
    return sum(lst) / len(lst)

def student_average(n, lst):
    return average(lst)

def main():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        name, *line = line
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print("{:.2f}".format(student_average(student_marks[query_name])))

if __name__ == '__main__':
    main()

