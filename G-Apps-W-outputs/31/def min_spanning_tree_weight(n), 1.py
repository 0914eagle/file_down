
def min_spanning_tree_weight(n):
    def highest_bit_position(num):
        pos = -1
        while num:
            pos += 1
            num >>= 1
        return pos
    
    if n == 2:
        return 0
    
    highest_bit = highest_bit_position(n)
    msb = 1 << highest_bit
    mask = msb - 1
    weight = (msb - 1) * (n - msb)
    weight += min_spanning_tree_weight(n - msb) + mask
    return weight

n = int(input())
print(min_spanning_tree_weight(n))
