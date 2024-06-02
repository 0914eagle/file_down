
def max_elements_in_array(p):
    n = len(p)
    if n == 1:
        return 1

    def can_split_into_two_numbers(num):
        for i in range(1, len(num)):
            a = int(num[:i])
            b = int(num[i:])
            if a != 0 and b != 0 and a < b:
                return True
        return False

    def find_max_elements(num):
        if not can_split_into_two_numbers(num):
            return 1
        max_elements = 1
        for i in range(1, len(num)):
            a = int(num[:i])
            b = int(num[i:])
            if a != 0 and b != 0 and a < b:
                max_elements = max(max_elements, 1 + find_max_elements(str(a)) + find_max_elements(str(b)))
        return max_elements

    return find_max_elements(p)

# Read input
p = input().strip()

# Call the function and print the result
print(max_elements_in_array(p))
