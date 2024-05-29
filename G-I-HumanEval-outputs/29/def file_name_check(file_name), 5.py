
def file_name_check(file_name):
    # Check if file name contains exactly one dot
    if file_name.count('.') != 1:
        return 'No'
    
    file_parts = file_name.split('.')
    
    # Check if there are more than three digits in the file name
    if sum(c.isdigit() for c in file_name) > 3:
        return 'No'
    
    # Check if the substring after the dot is one of ['txt', 'exe', 'dll']
    if file_parts[-1] not in ['txt', 'exe', 'dll']:
        return 'No'
    
    # Check if the substring before the dot is not empty and starts with a letter
    if not file_parts[0] or not file_parts[0][0].isalpha():
        return 'No'
    
    return 'Yes'

# Test cases
print(file_name_check("example.txt"))  # => 'Yes'
print(file_name_check("1example.dll"))  # => 'No'
print(file_name_check("myfile.dll"))  # => 'Yes'
print(file_name_check("name_with_more_than_3_digits123.exe"))  # => 'No'
```
