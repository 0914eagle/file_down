
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
                process_positions[process] = []
            process_positions[process].append(i)

    for process, positions in process_positions.items():
        for i in range(len(positions)):
            if positions[i] != free_positions[i]:
                operations += 1

    return operations

# Input
n = int(input())
cells = list(map(int, input().split()))

# Output
print(defragment_memory(n, cells))
