
def pronounce_counter_word(n):
    last_digit = n % 10
    if last_digit in [2, 4, 5, 7, 9]:
        return "hon"
    elif last_digit in [0, 1, 6, 8]:
        return "pon"
    elif last_digit == 3:
        return "bon"

# Taking input from Standard Input
n = int(input())

# Output the pronunciation of "本" based on the number
print(pronounce_counter_word(n))
