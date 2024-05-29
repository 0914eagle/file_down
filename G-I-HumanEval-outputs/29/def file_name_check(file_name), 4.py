
def file_name_check(file_name):
    if file_name.count('.') != 1:
        return 'No'
    
    name_parts = file_name.split('.')
    if len(name_parts) != 2:
        return 'No'
    
    if not name_parts[0] or not name_parts[1]:
        return 'No'
    
    if not name_parts[0][0].isalpha():
        return 'No'
    
    if not name_parts[1] in ['txt', 'exe', 'dll']:
        return 'No'
    
    digit_count = sum(c.isdigit() for c in file_name)
    if digit_count > 3:
        return 'No'
    
    return 'Yes'
