
import sys
import csv
from collections import namedtuple

def calculate_average(marks):
    return round(sum(marks)/len(marks), 2)

def main():
    n = int(sys.stdin.readline().strip())
    if n > 100:
        return
    marks = []
    with open(sys.argv[1], 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            marks.append(int(row['MARKS']))
    print(calculate_average(marks))

if __name__ == '__main__':
    main()

