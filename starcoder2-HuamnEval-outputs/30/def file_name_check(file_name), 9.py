
def file_name_check(file_name):
    if file_name.count('.') != 1:
        return 'No'
    if file_name.count('.') > 3:
        return 'No'
    if file_name.startswith('.'):
        return 'No'
    if file_name.endswith('.'):
        return 'No'
    if file_name.endswith('.txt') or file_name.endswith('.exe') or file_name.endswith('.dll'):
        return 'Yes'
    else:
        return 'No'
 