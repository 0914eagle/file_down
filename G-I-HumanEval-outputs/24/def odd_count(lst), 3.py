
def odd_count(lst):
    result = []
    for num_str in lst:
        odd_count = sum([1 for digit in num_str if int(digit) % 2 != 0])
        result.append("the number of odd elements {}n the str{}ng {} of the {}nput.".format(
            odd_count, odd_count, odd_count, odd_count))
    return result
