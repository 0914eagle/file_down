
def triples_sum_to_zero(l: list):
    for i in range(len(l) - 2):
        for j in range(i+1, len(l) - 1):
            for k in range(j+1, len(l)):
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False

# Test cases
print(triples_sum_to_zero([1, 3, 5, 0]))  # False
print(triples_sum_to_zero([1, 3, -2, 1]))  # True
print(triples_sum_to_zero([1, 2, 3, 7]))  # False
print(triples_sum_to_zero([2, 4, -5, 3, 9, 7]))  # True
print(triples_sum_to_zero([1]))  # False
