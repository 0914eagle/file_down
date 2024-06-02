
def is_adorable(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    for key in freq:
        if freq[key] >= 2:
            return "Yes"

    return "No"

# Input
s = input().strip()

# Output
print(is_adorable(s))
