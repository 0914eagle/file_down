
def find_min_spanning_tree_weight(n):
    def get_bit(x, i):
        return (x >> i) & 1

    def set_bit(x, i):
        return x | (1 << i)

    weight = 0
    for i in range(1, n):
        u = 0
        v = i
        xor_result = u ^ v
        msb_position = 0
        while xor_result:
            xor_result >>= 1
            msb_position += 1
        weight += 1 << (msb_position - 1)
    return weight

n = int(input())
print(find_min_spanning_tree_weight(n))
