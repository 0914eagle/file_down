
 def rescale_to_unit(numbers):
    min_number = min(numbers)
    max_number = max(numbers)
    return [(number - min_number) / (max_number - min_number) for number in numbers]
 