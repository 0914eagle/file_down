
def split_words(txt):
    if ' ' in txt:
        return txt.split(' ')
    elif ',' in txt:
        return txt.split(',')
    else:
        return sum(1 for i in txt if ord(i) % 2 == 1)
 