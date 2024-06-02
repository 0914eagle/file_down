
class Employee:
    def __init__(self, id, salary, height):
        self.id = id
        self.salary = salary
        self.height = height
        self.boss = None
        self.subordinates = []

def find_boss_and_subordinates(employees, query_id):
    for employee in employees:
        if employee.id == query_id:
            boss_id = 0 if employee.boss is None else employee.boss.id
            return boss_id, len(employee.subordinates)
    return None, None

def main():
    m, q = map(int, input().split())
    employees = []
    
    for _ in range(m):
        id, salary, height = map(int, input().split())
        employees.append(Employee(id, salary, height))
    
    employees.sort(key=lambda x: (-x.salary, -x.height))
    
    for i in range(1, m):
        for j in range(i-1, -1, -1):
            if employees[j].height >= employees[i].height:
                employees[i].boss = employees[j]
                employees[j].subordinates.append(employees[i])
                break
    
    for _ in range(q):
        query_id = int(input())
        boss_id, num_subordinates = find_boss_and_subordinates(employees, query_id)
        print(f"{boss_id} {num_subordinates}")

if __name__ == "__main__":
    main()
