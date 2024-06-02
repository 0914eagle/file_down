
def file_name_check(file_name):
    if file_name.count('.') != 1:
        return 'No'
    else:
        file_name_split = file_name.split('.')
        if file_name_split[0].isalpha() == False:
            return 'No'
        elif file_name_split[1] not in ['txt', 'exe', 'dll']:
            return 'No'
        elif file_name_split[0].isdigit() == True:
            return 'No'
        elif file_name_split[0].count('0') + file_name_split[0].count('1') + file_name_split[0].count('2') + file_name_split[0].count('3') + file_name_split[0].count('4') + file_name_split[0].count('5') + file_name_split[0].count('6') + file_name_split[0].count('7') + file_name_split[0].count('8') + file_name_split[0].count('9') > 3:
            return 'No'
        else:
            return 'Yes'
 