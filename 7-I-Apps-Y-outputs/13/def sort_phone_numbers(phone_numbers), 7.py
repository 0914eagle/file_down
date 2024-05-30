
def sort_phone_numbers(phone_numbers):
    return sorted(phone_numbers, key=lambda x: int(x[2:]))

if __name__ == '__main__':
    phone_numbers = []
    for _ in range(int(input())):
        phone_numbers.append(input())
    print(*sort_phone_numbers(phone_numbers), sep='\n')

