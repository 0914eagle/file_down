
def decorator(func):
    def wrapper(*args, **kwargs):
        print("+91 ", end="")
        return func(*args, **kwargs)
    return wrapper

@decorator
def print_mobile_numbers(numbers):
    for num in numbers:
        print(num, end=" ")

if __name__ == "__main__":
    n = int(input())
    numbers = []
    for _ in range(n):
        numbers.append(input())
    print_mobile_numbers(numbers)

