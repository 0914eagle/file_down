
def reverse_binary(n):
    binary = bin(n)[2:]
    reversed_binary = binary[::-1]
    return int(reversed_binary, 2)
