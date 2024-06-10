
import math

def count_numbers_in_row(row_number, number):
    if number == 1:
        return 1
    
    if number < row_number:
        return 0
    
    number_of_digits = len(str(number))
    
    if number_of_digits == 1:
        return 1
    
    first_digit = int(number / (10 ** (number_of_digits - 1)))
    
    if first_digit == 1:
        return 1 + count_numbers_in_row(row_number, number % (10 ** (number_of_digits - 1)))
    
    return count_numbers_in_row(row_number, number - (10 ** (number_of_digits - 1)))
    
def count_numbers(A, B):
    row_number = math.ceil(math.sqrt(A))
    
    number_of_appearances = 0
    
    while row_number ** 2 <= B:
        number_of_appearances += count_numbers_in_row(row_number, B) - count_numbers_in_row(row_number, A - 1)
        
        row_number += 1
    
    return number_of_appearances
    
def main():
    Q = int(input())
    
    for i in range(Q):
        A, B = map(int, input().split())
        
        print(count_numbers(A, B))
    
if __name__ == '__main__':
    main()
    

