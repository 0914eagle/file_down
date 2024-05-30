
def min_char(route):
    if route.count('M') == 0:
        return len(route)
    else:
        macro = route.split('M')
        macro_len = 0
        for i in range(len(macro)):
            macro_len += len(macro[i])
        return macro_len + 2

route = input()
print(min_char(route))

