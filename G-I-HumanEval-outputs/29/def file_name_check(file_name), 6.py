
def file_name_check(file_name):
    # Check condition 1: not more than three digits
    if sum(1 for char in file_name if char.isdigit()) > 3:
        return 'No'

    # Check condition 2: contains exactly one dot
    if file_name.count('.') != 1:
        return 'No'

    # Split file_name into name and extension
    name, extension = file_name.rsplit('.', 1)

    # Check condition 3: name starts with a letter
    if not name or not name[0].isalpha():
        return 'No'

    # Check condition 4: extension is one of ['txt', 'exe', 'dll']
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

# Test cases
print(file_name_check("example.txt"))  # => 'Yes'
print(file_name_check("1example.dll"))  # => 'No'
```
