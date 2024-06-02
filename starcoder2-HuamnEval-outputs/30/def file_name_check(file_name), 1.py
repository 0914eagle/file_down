
 def file_name_check(file_name):
    if file_name.count('.') != 1:
        return 'No'
    if file_name.count('.') == 1:
        if file_name.count('.') > 3:
            return 'No'
        if file_name[0].isalpha() == False:
            return 'No'
        if file_name.split('.')[1] not in ['txt', 'exe', 'dll']:
            return 'No'
        else:
            return 'Yes'
 