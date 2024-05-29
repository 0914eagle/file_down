
def file_name_check(file_name):
    if len(file_name.split('.')) != 2:
        return 'No'
    
    name, extension = file_name.split('.')
    
    if not name or not name[0].isalpha():
        return 'No'
    
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'
    
    count_digits = sum(c.isdigit() for c in name)
    if count_digits > 3:
        return 'No'
    
    return 'Yes'

# Test cases
print(file_name_check("example.txt"))  # => 'Yes'
print(file_name_check("1example.dll"))  # => 'No'
print(file_name_check("file_123.exe"))  # => 'No'
```
