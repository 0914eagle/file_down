

# Generated with smolCode's lorem ipsum generator
def FirstOrSecond(array):
	sumFirst = 0
	sumSecond = 0
	for i in array:
		if i > 0:
			sumFirst += i
		elif i < 0:
			sumSecond += i
		if sumFirst > sumSecond:
			return "First"
		elif sumFirst < sumSecond:
			return "Second"
		elif sumFirst == sumSecond:
			if i > 0:
				return "First"
			elif i < 0:
				return "Second"
	return 0

if __name__ == '__main__':
    arr = [-1,-2,3]
    print(FirstOrSecond(arr))

