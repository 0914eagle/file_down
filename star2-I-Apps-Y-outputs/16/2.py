
def reverse_binary(n):
    binary = bin(n)[2:]
    reversed_binary = binary[::-1]
    reversed_number = int(reversed_binary, 2)
    return reversed_number

