
# Read the string
s = input()

# Initialize the maximum count
max_count = 0

# Initialize the maximum two-gram
max_two_gram = ''

# Iterate over all two-grams
for i in range(len(s) - 1):
    two_gram = s[i:i+2]
    count = s.count(two_gram)
    if count > max_count:
        max_count = count
        max_two_gram = two_gram

# Print the maximum two-gram
print(max_two_gram)

