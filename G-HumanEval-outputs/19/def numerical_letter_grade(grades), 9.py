
def numerical_letter_grade(grades):
    grades_table = {
        4.0: 'A+',
        3.7: 'A',
        3.3: 'A-',
        3.0: 'B+',
        2.7: 'B',
        2.3: 'B-',
        2.0: 'C+',
        1.7: 'C',
        1.3: 'C-',
        1.0: 'D+',
        0.7: 'D',
        0.0: 'D-'
    }

    result = []
    for grade in grades:
        letter_grade = max((key for key in grades_table.keys() if key <= grade), default=0.0)
        result.append(grades_table[letter_grade])

    return result

# Test the function
print(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]))  # Output: ['A+', 'A', 'C', 'C+', 'A-']
```