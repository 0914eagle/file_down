
def file_name_check(file_name):
    if file_name.count('.') != 1:
        return 'No'

    name, extension = file_name.split('.')
    if not name or not extension:
        return 'No'

    if not name[0].isalpha():
        return 'No'

    if extension not in ['txt', 'exe', 'dll']:
        return 'No'

    if sum(c.isdigit() for c in file_name) > 3:
        return 'No'

    return 'Yes'

# Test cases
print(file_name_check("example.txt"))  # => 'Yes'
print(file_name_check("1example.dll"))  # => 'No'
