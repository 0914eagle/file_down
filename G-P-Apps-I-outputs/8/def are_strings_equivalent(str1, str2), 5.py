
def are_strings_equivalent(str1, str2):
    if str1 == str2:
        return True
    
    n = len(str1)
    
    # Check if strings can be split into equivalent halves
    if n % 2 == 0:
        first_half_str1 = str1[:n//2]
        second_half_str1 = str1[n//2:]
        
        first_half_str2 = str2[:n//2]
        second_half_str2 = str2[n//2:]
        
        if (are_strings_equivalent(first_half_str1, first_half_str2) and 
            are_strings_equivalent(second_half_str1, second_half_str2)):
            return True
        
        if (are_strings_equivalent(first_half_str1, second_half_str2) and 
            are_strings_equivalent(second_half_str1, first_half_str2)):
            return True
    
    return False

# Read input strings
str1 = input()
str2 = input()

# Check if strings are equivalent
if are_strings_equivalent(str1, str2):
    print("YES")
else:
    print("NO")
```
