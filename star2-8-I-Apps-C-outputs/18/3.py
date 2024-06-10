
def main():
    m, q = map(int, input().split())
    employees = dict()
    for _ in range(m):
        id, salary, height = map(int, input().split())
        employees[id] = {"salary": salary, "height": height, "boss": None, "subordinates": 0}
    for _ in range(q):
        id = int(input())
        for employee_id in employees:
            if employees[employee_id]["salary"] > employees[id]["salary"] and employees[employee_id]["height"] >= employees[id]["height"]:
                employees[id]["boss"] = employee_id
                employees[employee_id]["subordinates"] += 1
        if employees[id]["boss"] is None:
            print(0, 0)
        else:
            print(employees[id]["boss"], employees[id]["subordinates"])


if __name__ == "__main__":
    main()

