
def count_permutations(n, adj_matrix):
    total_perms = 1 << (n - 1)
    results = [0] * total_perms

    for perm in range(1, total_perms):
        set_bits = bin(perm).count('1')
        for i in range(n - 1):
            if (perm & (1 << i)) > 0:
                continue

            valid_perm = True
            for j in range(i + 1, n - 1):
                if (perm & (1 << j)) == 0:
                    continue

                if adj_matrix[set_bits - 1][j] != '1':
                    valid_perm = False
                    break

            if valid_perm:
                results[perm] += 1

    return results

n = int(input())
adj_matrix = [input() for _ in range(n)]

results = count_permutations(n, adj_matrix)
print(' '.join(map(str, results)))
