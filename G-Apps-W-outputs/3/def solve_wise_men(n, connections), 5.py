
def solve_wise_men(n, connections):
    def get_binary_strings(n):
        binary_strings = []
        for i in range(2**(n-1)):
            binary_strings.append(bin(i)[2:].zfill(n-1))
        return binary_strings

    def count_permutations(binary_string):
        count = 0
        for perm in permutations:
            valid = True
            for i in range(n-1):
                if (binary_string[i] == '1' and connections[perm[i]][perm[i+1]] != '1') or (binary_string[i] == '0' and connections[perm[i]][perm[i+1]] != '0'):
                    valid = False
                    break
            if valid:
                count += 1
        return count

    permutations = list(itertools.permutations(range(n)))
    binary_strings = get_binary_strings(n)

    result = []
    for binary_string in binary_strings:
        result.append(count_permutations(binary_string))

    return result

# Input
n = int(input())
connections = []
for _ in range(n):
    connections.append(input().strip())

# Output
output = solve_wise_men(n, connections)
print(*output)
