
def main():
    n = int(input())
    task_list = []
    for _ in range(n):
        task_list.append(list(map(int, input().split())))
    max_size = 0
    queue = []
    for task in task_list:
        queue += list(range(task[0], task[0] + task[1]))
        if max_size < len(queue):
            max_size = len(queue)
        queue = queue[1:]
    print(queue[-1], max_size)
if __name__ == "__main__":
    main()
