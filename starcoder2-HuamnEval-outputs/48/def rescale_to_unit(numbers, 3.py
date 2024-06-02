
 def rescale_to_unit(numbers: List[float]) -> List[float]:
    
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements")
    min_number = min(numbers)
    max_number = max(numbers)
    return [(number - min_number) / (max_number - min_number) for number in numbers]
 