
 def file_name_check(file_name):
    if file_name.count('.') != 1:
        return 'No'
    if file_name.count('.') == 1:
        if file_name.count('0') + file_name.count('1') + file_name.count('2') + file_name.count('3') + file_name.count('4') + file_name.count('5') + file_name.count('6') + file_name.count('7') + file_name.count('8') + file_name.count('9') > 3:
            return 'No'
        if file_name.split('.')[0][0] not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            return 'No'
        if file_name.split('.')[1] not in ['txt', 'exe', 'dll']:
            return 'No'
        else:
            return 'Yes'
 