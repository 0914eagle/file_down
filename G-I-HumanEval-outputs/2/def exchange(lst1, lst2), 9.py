
def exchange(lst1, lst2):
    # Count the number of odd elements in lst1
    count_odd_lst1 = sum(1 for num in lst1 if num % 2 == 1)
    
    # Count the number of odd elements in lst2
    count_odd_lst2 = sum(1 for num in lst2 if num % 2 == 1)
    
    # If there are enough odd elements in lst2 to exchange with odd elements in lst1
    if count_odd_lst2 >= count_odd_lst1:
        return "YES"
    else:
        return "NO"

# Test cases
print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))  # Should return "YES"
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))  # Should return "NO"
