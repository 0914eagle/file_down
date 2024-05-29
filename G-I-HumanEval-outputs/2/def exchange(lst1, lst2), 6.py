
def exchange(lst1, lst2):
    # Count the number of odd elements in lst1
    odd_count = sum(1 for x in lst1 if x % 2 != 0)
    
    # Check if we can exchange elements to make all elements of lst1 even
    # We can do this if the total count of odd elements in lst1 and lst2 is even (as each exchange can make two elements even)
    if (odd_count + sum(1 for x in lst2 if x % 2 != 0)) % 2 == 0:
        return "YES"
    else:
        return "NO"

# Test cases
print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))  # Should return "YES"
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))  # Should return "NO"
