
s = input()
s = s.replace('=', '')
s = s.replace('^', '')
if s == '1':
	print('balance')
else:
	print('left' if int(s) % 9 > 4 else 'right')
