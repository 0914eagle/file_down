
def find_max_lucky_number(n):
    
    count = 0
    max_lucky_number = 0
    while count < 10 ** n:
        number = str(count)
        if all(digit in "78" for digit in number):
            max_lucky_number = count
        count += 1
    return max_lucky_number


if __name__ == "__main__":
    n = int(input())
    print(find_max_lucky_number(n))

