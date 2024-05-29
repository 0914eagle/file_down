
def file_name_check(file_name):
    # Check condition 1: Not more than three digits in the file's name
    if sum(c.isdigit() for c in file_name) > 3:
        return 'No'
    
    # Check condition 2: One dot in the file's name
    if file_name.count('.') != 1:
        return 'No'
    
    # Split the file name into parts before and after the dot
    before_dot, after_dot = file_name.split('.')
    
    # Check condition 3: Substring before the dot starts with a letter from the latin alphabet
    if not before_dot or not before_dot[0].isalpha():
        return 'No'
    
    # Check condition 4: Substring after the dot is one of ['txt', 'exe', 'dll']
    if after_dot not in ['txt', 'exe', 'dll']:
        return 'No'
    
    return 'Yes'

# Testing the function
print(file_name_check("example.txt"))  # Should print 'Yes'
print(file_name_check("1example.dll"))  # Should print 'No'
```
