
n = int(input())
binary = bin(n)[2:]
reversed_binary = binary[::-1]
reversed_number = int(reversed_binary, 2)
print(reversed_number)

