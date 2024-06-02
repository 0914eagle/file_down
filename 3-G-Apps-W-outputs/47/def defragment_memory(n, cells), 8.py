
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
                process_positions[process] = [i]
            else:
                process_positions[process].append(i)

    for process in process_positions:
        positions = process_positions[process]
        for i in range(len(positions)):
            if positions[i] != free_positions[i]:
                operations += 1

    return operations

# Input processing
n = int(input())
cells = list(map(int, input().split()))

# Call the function and print the result
result = defragment_memory(n, cells)
print(result)
