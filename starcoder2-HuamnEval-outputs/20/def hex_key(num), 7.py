
def hex_key(num):
    return sum(1 for i in num if int(i, 16) in [2, 3, 5, 7, 11, 13])
 