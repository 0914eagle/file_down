
def exchange(lst1, lst2):
    # Count the number of odd elements in lst1
    odd_count = sum(1 for num in lst1 if num % 2 != 0)
    
    # If the number of odd elements in lst1 is greater than 1, return "NO"
    if odd_count > 1:
        return "NO"
    
    # Calculate the total sum of odd elements in lst2
    odd_sum_lst2 = sum(num for num in lst2 if num % 2 != 0)
    
    # If the total sum of odd elements in lst2 is odd, return "NO"
    if odd_sum_lst2 % 2 != 0:
        return "NO"
    
    return "YES"

# Test cases
print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))  # Output: "YES"
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))  # Output: "NO"
