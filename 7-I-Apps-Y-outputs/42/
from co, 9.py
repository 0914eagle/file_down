
from collections import namedtuple

N = int(input())

Student = namedtuple('Student','ID MARKS CLASS NAME')

Student_list = []

for i in range(N):
    line = input().split()
    Student_list.append(Student(line[0],line[1],line[2],line[3]))

print('%.2f' %(sum([int(student.MARKS) for student in Student_list])/N))

