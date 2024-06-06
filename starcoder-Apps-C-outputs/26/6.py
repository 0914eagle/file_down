
n = int(input())
field = list(input())

i = 0
while i < len(field):
    if field[i] == 'P':
        field[i] = '.'
        i -= 1
    i += 1
print(field.count('*'))
