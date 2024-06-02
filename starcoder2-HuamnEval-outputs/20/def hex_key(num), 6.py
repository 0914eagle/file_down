
 def hex_key(num):
    hex_num = '0123456789ABCDEF'
    prime_num = '2357BDF'
    count = 0
    for i in num:
        if i in prime_num:
            count += 1
    return count
 