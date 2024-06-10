
import sys

def binarySearch(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid][1] == x:
            return mid
        elif arr[mid][1] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

def main():
    m, q = map(int, input().split())
    employees = [None for i in range(m)]
    for i in range(m):
        employees[i] = list(map(int, input().split()))
    employees.sort(key=lambda x: x[2])

    queries = [None for i in range(q)]
    for i in range(q):
        queries[i] = int(input())

    for query in queries:
        idx = binarySearch(employees, 0, m - 1, query)
        if idx != -1:
            height = employees[idx][2]
            salary = employees[idx][1]
            subordinates = 0
            for j in range(idx + 1, m):
                if employees[j][2] > height and employees[j][1] > salary:
                    subordinates += 1
            print("{} {}".format(employees[idx - 1][0], subordinates))
        else:
            print("No such employee")

if __name__ == "__main__":
    main()

