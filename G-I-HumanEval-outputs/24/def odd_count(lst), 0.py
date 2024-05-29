
def odd_count(lst):
    result = []
    for string in lst:
        count = sum([1 for char in string if int(char) % 2 != 0])
        result.append("the number of odd elements {}n the str{}ng {} of the {}nput.".format(count, count, count, count))

    return result

# Test cases
print(odd_count(['1234567']))
print(odd_count(['3', '11111111']))
