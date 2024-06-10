
def reverse_binary(num):
    binary = bin(num)[2:]
    reversed_binary = binary[::-1]
    reversed_num = int(reversed_binary, 2)
    return reversed_num

n = int(input())
reversed_n = reverse_binary(n)
print(reversed_n)

