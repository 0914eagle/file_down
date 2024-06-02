
def hex_key(num):
    return sum(1 for x in num if int(x, 16) in {2, 3, 5, 7, 11, 13, 17})
 