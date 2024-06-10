
import sys
input = sys.stdin.readline
def main():
    m, q = map(int, input().split())
    employees = [0] * m
    for i in range(m):
        ID, salary, height = map(int, input().split())
        employees[i] = (ID, salary, height)
    for _ in range(q):
        ID = int(input())
        e_id, e_salary, e_height = employees[0]
        for e in employees:
            if e[0] == ID:
                e_id, e_salary, e_height = e
                break
        immediate_boss = None
        for e in employees:
            if e[1] < e_salary and e[2] >= e_height:
                immediate_boss = e
                break
        if immediate_boss is None:
            print(0, 0)
        else:
            subordinates = 0
            for e in employees:
                if e[1] > immediate_boss[1] and e[2] >= immediate_boss[2]:
                    subordinates += 1
            print(immediate_boss[0], subordinates)
main()

