
def check_if_last_char_is_a_letter(txt):
    if txt.endswith(' '):
        return False
    else:
        return txt[-1].isalpha()
 