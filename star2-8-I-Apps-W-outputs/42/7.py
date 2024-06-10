
def magic_number(a, b, m, d):
    a_list = [int(x) for x in a]
    b_list = [int(x) for x in b]
    modulus = pow(10, 9) + 7
    count = 0
    for num in range(a, b + 1):
        num_list = [int(x) for x in str(num)]
        if num % m == 0:
            i = 0
            while i < len(num_list):
                if num_list[i] == d:
                    i += 2
                else:
                    break
            if i == len(num_list):
                count += 1
    return count % modulus


m, d = [int(x) for x in input().split()]
a = int(input())
b = int(input())
print(magic_number(a, b, m, d))

