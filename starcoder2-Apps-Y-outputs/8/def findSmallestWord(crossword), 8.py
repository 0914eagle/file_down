
# Python 3 program to find the lexicographically smallest word
# in a crossword puzzle

# Function to find the lexicographically smallest word
def findSmallestWord(crossword):

	# Initialize result
	result = ""

	# Traverse through all rows
	for i in range(R):

		# Traverse through all columns
		for j in range(C):

			# If current character is empty
			if (crossword[i][j] == '#'):
				continue

			# Find words formed by moving downwards
			temp = ""
			k = i
			while (k < R and crossword[k][j] != '#'):
				temp += crossword[k][j]
				k += 1

			# Update result if current word is smaller
			if (len(temp) > 1 and temp < result):
				result = temp

			# Find words formed by moving right
			temp = ""
			k = j
			while (k < C and crossword[i][k] != '#'):
				temp += crossword[i][k]
				k += 1

			# Update result if current word is smaller
			if (len(temp) > 1 and temp < result):
				result = temp

	return result

# Driver code

# Given crossword
crossword = [
	['l', 'u', 'k', 'a'],
	['o', '#', 'a', '#'],
	['k', 'u', 'l', 'a'],
	['i', '#', 'a', '#']
]

# Size of crossword
R = 4
C = 4

# Find the lexicographically smallest word
print(findSmallestWord(crossword))

# This code is contributed by 

