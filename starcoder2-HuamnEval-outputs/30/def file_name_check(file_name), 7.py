
 def file_name_check(file_name):
    if file_name.count('.') != 1:
        return 'No'
    if file_name.count('.') == 1:
        if file_name.count('.') > 3:
            return 'No'
        if file_name.count('.') == 1:
            if file_name[0].isalpha():
                if file_name.split('.')[1] in ['txt', 'exe', 'dll']:
                    return 'Yes'
                else:
                    return 'No'
            else:
                return 'No'
 