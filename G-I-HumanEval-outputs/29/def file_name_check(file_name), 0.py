
def file_name_check(file_name):
    valid_extensions = ['txt', 'exe', 'dll']
    
    if len(file_name.split('.')) != 2:
        return 'No'
    
    name_parts = file_name.split('.')
    if len(name_parts[0]) == 0 or not name_parts[0][0].isalpha():
        return 'No'
    
    if name_parts[1] not in valid_extensions:
        return 'No'
    
    digit_count = sum(1 for char in file_name if char.isdigit())
    if digit_count > 3:
        return 'No'
    
    return 'Yes'

# Test examples
print(file_name_check("example.txt")) # => 'Yes'
print(file_name_check("1example.dll")) # => 'No'
