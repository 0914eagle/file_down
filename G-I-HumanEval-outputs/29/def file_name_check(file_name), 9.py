
def file_name_check(file_name):
    if file_name.count('.') != 1:
        return 'No'
    
    parts = file_name.split('.')
    if len(parts) != 2:
        return 'No'
    
    if not parts[0].replace('.', '').isalpha():
        return 'No'
    
    if len([c for c in parts[0] if c.isdigit()]) > 3:
        return 'No'
    
    if parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    
    return 'Yes'

# Testing the function
print(file_name_check("example.txt"))  # => 'Yes'
print(file_name_check("1example.dll"))  # => 'No'
