
def defragment_memory(n, cells):
    process_positions = {}
    free_positions = []
    operations = 0

    for i in range(n):
        if cells[i] == 0:
            free_positions.append(i)
        else:
            process = cells[i]
            if process not in process_positions:
                process_positions[process] = [i, i]
            else:
                process_positions[process][1] = i

    for process in sorted(process_positions.keys()):
        start, end = process_positions[process]
        for i in range(start, end+1):
            if cells[i] == 0:
                operations += 1
                cells[i] = process
                cells[free_positions.pop(0)] = 0

    return operations

# Input
n = int(input())
cells = list(map(int, input().split()))

# Output
print(defragment_memory(n, cells))
