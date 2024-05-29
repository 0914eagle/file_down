
def file_name_check(file_name):
    # Check condition 1: No more than three digits
    if sum(c.isdigit() for c in file_name) > 3:
        return 'No'

    # Check condition 2: Exactly one dot
    if file_name.count('.') != 1:
        return 'No'

    # Split the file name into name and extension
    file_parts = file_name.split('.')
    if len(file_parts) != 2:
        return 'No'

    name_part, ext_part = file_parts

    # Check condition 3: Substring before dot starts with a letter
    if not name_part or not name_part[0].isalpha():
        return 'No'

    # Check condition 4: Extension is one of ['txt', 'exe', 'dll']
    if ext_part not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

# Test examples
print(file_name_check("example.txt"))  # => 'Yes'
print(file_name_check("1example.dll"))  # => 'No'
```
