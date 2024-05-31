
def digitSum(s):
    sum_upper = 0
    for char in s:
        if char.isupper():
            sum_upper += ord(char)
    return sum_upper

# Test cases
print(digitSum(""))  # 0
print(digitSum("abAB"))  # 131
print(digitSum("abcCd"))  # 67
print(digitSum("helloE"))  # 69
print(digitSum("woArBld"))  # 131
print(digitSum("aAaaaXa"))  # 153
