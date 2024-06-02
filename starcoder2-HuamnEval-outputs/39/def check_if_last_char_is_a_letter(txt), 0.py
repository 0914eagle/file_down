
def check_if_last_char_is_a_letter(txt):
    if txt[-1] == ' ' or txt == '':
        return False
    else:
        return True

print(check_if_last_char_is_a_letter("apple pie"))
print(check_if_last_char_is_a_letter("apple pi e"))
print(check_if_last_char_is_a_letter("apple pi e "))
print(check_if_last_char_is_a_letter(""))
 