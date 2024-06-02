
def defragment_memory(n, cells):
    process_positions = {}
    operations = 0

    for i in range(n):
        if cells[i] != 0:
            process = cells[i]
            if process not in process_positions:
                process_positions[process] = i
            else:
                operations += i - process_positions[process]
                process_positions[process] += 1

    return operations

# Input
n = int(input())
cells = list(map(int, input().split()))

# Output
print(defragment_memory(n, cells))
