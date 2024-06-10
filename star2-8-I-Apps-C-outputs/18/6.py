
def find_boss(employees, id):
    for employee in employees:
        if employee.id == id:
            return employee
    return None


def find_subordinates(employees, id):
    result = []
    for employee in employees:
        if employee.boss_id == id:
            result.append(employee)
    return result


class Employee:
    def __init__(self, id, salary, height):
        self.id = id
        self.salary = salary
        self.height = height
        self.boss_id = None
        self.subordinates = []


def solve(employees, queries):
    result = []
    for query in queries:
        employee = find_boss(employees, query)
        if employee.boss_id is None:
            result.append((0, len(employee.subordinates)))
        else:
            result.append((employee.boss_id, len(employee.subordinates)))
    return result

