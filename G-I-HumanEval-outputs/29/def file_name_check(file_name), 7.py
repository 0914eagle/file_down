
def file_name_check(file_name):
    if len(file_name.split('.')) != 2:
        return 'No'
    
    name, extension = file_name.split('.')
    
    if not name.isalpha() or not name[0].isalpha():
        return 'No'
    
    if len([c for c in name if c.isdigit()]) > 3:
        return 'No'
    
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'
    
    return 'Yes'

# Test cases
print(file_name_check("example.txt"))  # => 'Yes'
print(file_name_check("1example.dll"))  # => 'No'
print(file_name_check("file.name.dll"))  # => 'No'
print(file_name_check("file.txt"))  # => 'No'
print(file_name_check("file1.txt"))  # => 'Yes'
print(file_name_check("file1example.txt"))  # => 'No'
