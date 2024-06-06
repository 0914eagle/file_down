
# read the input line
x = input()

# print the output
if x.endswith('po'):
    print('FILIPINO')
elif x.endswith('desu') or x.endswith('masu'):
    print('JAPANESE')
else:
    print('KOREAN')

