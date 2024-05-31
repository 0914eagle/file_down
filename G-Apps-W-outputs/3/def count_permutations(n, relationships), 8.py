
def count_permutations(n, relationships):
    def generate_permutations(n):
        permutations = []
        for i in range(1, n+1):
            permutations.append(i)
        return list(itertools.permutations(permutations))

    def generate_binary_string(permutation, relationships):
        binary_string = ""
        for i in range(n - 1):
            if relationships[permutation[i] - 1][permutation[i+1] - 1] == '1':
                binary_string += '1'
            else:
                binary_string += '0'
        return binary_string

    def count_strings(n, relationships):
        strings_count = {}
        permutations = generate_permutations(n)
        for permutation in permutations:
            binary_string = generate_binary_string(permutation, relationships)
            if binary_string in strings_count:
                strings_count[binary_string] += 1
            else:
                strings_count[binary_string] = 1
        return strings_count

    def get_binary_count(binary_string_count):
        counts = [0] * (2**(n-1))
        for k, v in binary_string_count.items():
            binary_num = int(k, 2)
            counts[binary_num] = v
        return counts

    import itertools
    binary_string_count = count_strings(n, relationships)
    counts = get_binary_count(binary_string_count)

    return counts

# Input
n = int(input())
relationships = []
for _ in range(n):
    relationships.append(input())

# Output
result = count_permutations(n, relationships)
print(*result)
