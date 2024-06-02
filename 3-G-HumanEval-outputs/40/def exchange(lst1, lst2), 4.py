
def exchange(lst1, lst2):
    # Check if lst1 already contains only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"

    # Calculate the sum of odd numbers in lst1
    odd_sum = sum(num for num in lst1 if num % 2 != 0)

    # Calculate the sum of odd numbers in lst2
    odd_sum += sum(num for num in lst2 if num % 2 != 0)

    # If the total sum of odd numbers is even, it means we can make all elements of lst1 even
    return "YES" if odd_sum % 2 == 0 else "NO"

# Test cases
print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))  # Output: "YES"
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))  # Output: "NO"
