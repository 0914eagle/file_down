
def odd_count(lst):
    result = []
    for string in lst:
        odd_count = sum(1 for num in string if int(num) % 2 != 0)
        result.append("the number of odd elements {}n the str{}ng {} of the {}nput.".format(odd_count, odd_count, odd_count, odd_count))
    return result

print(odd_count(['1234567']))
print(odd_count(['3', '11111111']))

